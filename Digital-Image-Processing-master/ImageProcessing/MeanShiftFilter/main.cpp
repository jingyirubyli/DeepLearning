#include <opencv2/opencv.hpp>

using namespace cv;
void callback(int, void*);

int spatialRad = 50;  // �ռ䴰�ڰ뾶
int colorRad = 50;   // ɫ�ʾ���
int maxPyrLevel = 2;  // ��˹����������

int main()
{
	Mat img = imread("D:\\TestData\\lena.jpg"); //����ͼ��  
	imshow("srcImg", img);

	// ������
	namedWindow("param");
	createTrackbar("sr", "param", &spatialRad, 50, callback, (void *)&img);
	createTrackbar("cr", "param", &colorRad, 50, callback, (void *)&img);

	// ��ʼ��
	callback(0, (void *)&img);

	// �ȴ��˳�
	waitKey(0);
	destroyAllWindows();

	return 0;
}

// �϶���call����
void callback(int, void* param) {
	Mat &img = *(Mat*)param; // ָ����任
	Mat res; // ���ͼ
	pyrMeanShiftFiltering(img, res, spatialRad, colorRad, maxPyrLevel); // ��ֵƯ���˲�

	// ��ʾ
	imshow("Result", res);
}