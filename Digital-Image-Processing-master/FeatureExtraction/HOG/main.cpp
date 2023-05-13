#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main()
{
	Mat image = imread("D:\\TestData\\test.jpg");
	// 1. ����HOG����
	HOGDescriptor hog(Size(64, 128), Size(16, 16), Size(8, 8), Size(8, 8), 9);//HOG���������������HOG�����ӵ�
	// 2. ����SVM������
	hog.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());   // �����Ѿ�ѵ���õ����˼�������
	// 3. �ڲ���ͼ���ϼ����������
	vector<cv::Rect> regions;
	hog.detectMultiScale(image, regions, 0, Size(8, 8), Size(32, 32), 1.05, 1);
	// ��ʾ
	for (size_t i = 0; i < regions.size(); i++)
	{
		rectangle(image, regions[i], Scalar(0, 0, 255), 2);
	}
	imshow("HOG���˼��", image);
	waitKey();

	return 0;
}