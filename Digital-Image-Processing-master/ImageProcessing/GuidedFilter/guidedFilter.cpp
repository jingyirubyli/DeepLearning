#include "guidedFilter.h"
#include <iostream>
#include <string>

using namespace std;
using namespace cv;


GuidedFilter::GuidedFilter()
{
}

GuidedFilter::~GuidedFilter()
{
}


//����ͼΪ�Ҷ�ͼ��
cv::Mat GuidedFilter::runGuidedFilter_Gray(cv::Mat I, cv::Mat P, int type, int radius, double eps)
{
	cv::Size winSize(2 * radius + 1, 2 * radius + 1);
	//��I*I, I*P
	cv::Mat  I2, IP;
	multiply(I, I, I2);
	multiply(I, P, IP);
	//���ֵ
	cv::Mat meanI, meanP, meanI2, meanIP;
	cv::boxFilter(I, meanI, type, winSize);
	cv::boxFilter(P, meanP, type, winSize);
	cv::boxFilter(I2, meanI2, type, winSize);
	cv::boxFilter(IP, meanIP, type, winSize);
	//�󷽲�/Э����
	cv::Mat varI, covIP;
	varI = meanI2 - meanI.mul(meanI);
	covIP = meanIP - meanI.mul(meanP);
	//��ϵ��a, b
	cv::Mat a, b;
	varI += eps;
	cv::divide(covIP, varI, a);
	b = meanP - a.mul(meanI);
	//a��b��������ƽ��
	cv::Mat meanA, meanB;
	cv::boxFilter(a, meanA, type, winSize);
	cv::boxFilter(b, meanB, type, winSize);
	//���
	cv::Mat output;
	output = meanA.mul(I) + meanB;
	return output;
}

//����ͼIΪ�Ҷ�ͼ������ͼ��PΪ��ͨ��������ͨ��ͼ��
cv::Mat GuidedFilter::myGuidedFilter_GrayGuided(cv::Mat guidedImg, cv::Mat inputImg, int radius, double eps)
{
	CV_Assert(guidedImg.channels() == 1);
	CV_Assert(inputImg.channels() == 1 || inputImg.channels() == 3);
	CV_Assert(guidedImg.rows == inputImg.rows && guidedImg.cols == inputImg.cols);
	int type = CV_64FC1;
	cv::Mat I, P, output;
	inputImg.convertTo(P, type);
	guidedImg.convertTo(I, type);

	//�ж�����ͼ���ǵ�ͨ��������ͨ��
	int channel = inputImg.channels();
	switch (channel)
	{
	case 1:
		output = runGuidedFilter_Gray(I, P, type, radius, eps);
		break;
	case 3:
	{
		cv::Mat bgr[3], bgrFilter[3];
		cv::split(P, bgr);
		for (int chan = 0; chan < channel; chan++)
		{
			bgrFilter[chan] = runGuidedFilter_Gray(I, bgr[chan], type, radius, eps);
		}
		cv::merge(bgrFilter, channel, output);
		break;
	}
	default:
		cout << "err! input image channel should be 1 or 3! " << endl;
		break;
	}

	return output;
}

//����ͼIΪ��ͨ��ͼ��
cv::Mat GuidedFilter::runGuidedFilter_Color(cv::Mat I, cv::Mat P, int type, int radius, double eps)
{
	cv::Size winSize(2 * radius + 1, 2 * radius + 1);
	int channel = I.channels();
	int H = I.rows;
	int W = I.cols;

	cv::Mat bgr[3], meanI[3];
	//����ͼ��ͨ���ľ�ֵ
	split(I, bgr);
	for (int chan = 0; chan < channel; chan++)
	{
		boxFilter(bgr[chan], meanI[chan], type, winSize);
	}
	//����ͼ���ֵ
	cv::Mat meanP;
	boxFilter(P, meanP, type, winSize);
	//����ͼ��ͨ��������ͼ����˲����ֵ
	cv::Mat meanIP[3], IP;
	for (int chan = 0; chan < channel; chan++)
	{
		multiply(bgr[chan], P, IP);
		boxFilter(IP, meanIP[chan], type, winSize);
	}
	//����ͼ��ͨ��������ͼЭ����
	cv::Mat covIP[3], meanImulP;
	for (int chan = 0; chan < channel; chan++)
	{
		multiply(meanI[chan], meanP, meanImulP);
		covIP[chan] = meanIP[chan] - meanImulP;
	}

	//������ͼЭ�������
	cv::Mat varI[9], tmp, mean2Tmp, meanTmp2;
	int varIdx = 0;
	for (int i = 0; i < channel; i++)
	{
		for (int j = 0; j < channel; j++)
		{
			multiply(bgr[i], bgr[j], tmp);
			boxFilter(tmp, meanTmp2, type, winSize);//mean(I*I)
			multiply(meanI[i], meanI[j], mean2Tmp);//meanI*meanI
			varI[varIdx] = meanTmp2 - mean2Tmp;
			varIdx++;
		}
	}
	//��a����ͨ��
	cv::Mat a[3];
	for (int chan = 0; chan < channel; chan++)
	{
		a[chan] = cv::Mat::zeros(I.size(), type);
	}
	cv::Mat epsEye = cv::Mat::eye(3, 3, type);
	epsEye *= eps;
	//��ʽ(19)
	for (int y = 0; y < H; y++)
	{
		double* vData[9];
		for (int v = 0; v < 9; v++)
		{
			vData[v] = (double*)varI[v].ptr<double>(y);
		}
		double* cData[3];
		for (int c = 0; c < 3; c++)
		{
			cData[c] = (double *)covIP[c].ptr<double>(y);
		}
		double* aData[3];
		for (int c = 0; c < 3; c++)
		{
			aData[c] = (double*)a[c].ptr<double>(y);
		}
		for (int x = 0; x < W; x++)
		{
			cv::Mat sigma = (cv::Mat_<double>(3, 3) <<
				vData[0][x], vData[1][x], vData[2][x],
				vData[3][x], vData[4][x], vData[5][x],
				vData[6][x], vData[7][x], vData[8][x]
				);
			sigma += epsEye;
			cv::Mat cov_Ip_13 = (cv::Mat_<double>(3, 1) <<
				cData[0][x], cData[1][x], cData[2][x]);
			cv::Mat tmpA = sigma.inv()*cov_Ip_13;
			double* tmpData = tmpA.ptr<double>(0);
			for (int c = 0; c < 3; c++)
			{
				aData[c][x] = tmpData[c];
			}
		}
	}

	//��b
	cv::Mat b = meanP - a[0].mul(meanI[0]) - a[1].mul(meanI[1]) - a[2].mul(meanI[2]);
	//b�ľ�ֵ
	cv::Mat meanB;
	boxFilter(b, meanB, type, winSize);
	//a�ľ�ֵ
	cv::Mat meanA[3];
	for (int c = 0; c < channel; c++)
	{
		boxFilter(a[c], meanA[c], type, winSize);
	}
	cv::Mat output = (meanA[0].mul(bgr[0]) + meanA[1].mul(bgr[1]) + meanA[2].mul(bgr[2])) + meanB;

	return output;
}

//����ͼIΪ��ͨ��ͼ������ͼ��PΪ��ͨ��������ͨ��ͼ��
cv::Mat GuidedFilter::myGuidedFilter_ColorGuided(cv::Mat guidedImg, cv::Mat inputImg, int radius, double eps)
{
	CV_Assert(guidedImg.channels() == 3);
	CV_Assert(inputImg.channels() == 1 || inputImg.channels() == 3);
	CV_Assert(guidedImg.cols == inputImg.cols && guidedImg.rows == inputImg.rows);
	int type = CV_64F;
	int channel = inputImg.channels();
	cv::Mat I, P, output;
	guidedImg.convertTo(I, type);
	inputImg.convertTo(P, type);

	//�ж�����ͼ���ǵ�ͨ��������ͨ��
	switch (channel)
	{
	case 1:
		output = runGuidedFilter_Color(I, P, type, radius, eps);
		break;
	case 3:
	{
		cv::Mat bgr[3], bgrFilter[3];
		cv::split(P, bgr);
		for (int chan = 0; chan < channel; chan++)
		{
			bgrFilter[chan] = runGuidedFilter_Color(I, bgr[chan], type, radius, eps);
		}
		cv::merge(bgrFilter, channel, output);
		break;
	}
	default:
		cout << "err! input image channel should be 1 or 3! " << endl;
		break;
	}

	output.convertTo(output, CV_8U);
	return output;
}
������
#include <opencv2\opencv.hpp>
#include "guidedFilter.h"
#include <iostream>

using namespace std;
using namespace cv;

int main(int argc, char** argv)
{
    //if (argc != 2)
    //{
    //    cout << "Usage: opencv_test <image path>" << endl;
    //    return -1;
    //}

    //char *imgName = argv[1]; 
	char *imgName = "C:\\Users\\VINNO\\Desktop\\src\\cat.jpg";
    Mat inputImg;

    inputImg = imread(imgName, 1);
    if (!inputImg.data)
    {
        cout << "No image data" << endl;
        return -1;
    }
    Mat grayImg , guidedImg;
	inputImg.copyTo(guidedImg);

	GuidedFilter filter;
	grayImg = filter.myGuidedFilter_ColorGuided(inputImg, guidedImg, 80, 0.001);
    imwrite("./result.jpg", grayImg);
	imshow("", grayImg);
	waitKey(0);

    return 0;
}