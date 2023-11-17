import cv2
import os

# 다운받은 이미지가 있는 디렉토리
base_dir = '/Users/bangseonghwan/Downloads/Traffic_light'
# 결과 분리 디렉토리
outputDir = '/Users/bangseonghwan/PycharmProjects/pythonProject1/output'
os.makedirs(outputDir, exist_ok=True)

def imageConvert() :
    # 루트 디텍토리 안의 폴더 저장
    directories = []
    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if os.path.isdir(folder_path):
            directories.append(folder)

    # 폴더안의 이미지, 텍스트 폴더 분류
    for folder in directories:
        # JPEGImages_mosaic은 폴더 이름
        imgDir = os.path.join(base_dir, folder, 'JPEGImages_mosaic')
        # labels_class_5는 폴더 이름
        textDir = os.path.join(base_dir, folder, 'labels_class_5')

        # 이미지들 저장
        images = []
        for file in os.listdir(imgDir):
            if file.endswith('.jpg'):
                file_path = os.path.join(imgDir, file)
                # print(file_path)
                images.append(file_path)

        # print(images)

        # 모든 이미지에 대한 코드
        for image in images:
            # 이미지, 텍스트 읽기
            img = cv2.imread(image)
            # print('image', image)
            # print('txt', os.path.split(os.path.basename(image))[1])
            txt = os.path.join(textDir, os.path.split(os.path.basename(image))[1][:-4] + '.txt')

            with open(txt, 'r') as file:
                lines = file.readlines()
                # 각 줄에 대해 작업
                for line in lines:
                    values = list(map(int, line.strip().split()))
                    left, top, right, bottom = values[:4]
                    # 범위내 픽셀
                    signalArea = img[top:bottom, left:right]
                    # 신호 정보
                    signInfo = str(values[4])

                    # 신호 정보에 대한 디렉토리 생성
                    signalDir = os.path.join(outputDir, signInfo)
                    os.makedirs(signalDir, exist_ok=True)

                    signalImgDir = os.path.join(signalDir, 'img')
                    signalTextDir = os.path.join(signalDir, 'text')
                    os.makedirs(signalImgDir, exist_ok=True)
                    os.makedirs(signalTextDir, exist_ok=True)
                    # 자른 이미지 저장
                    outputImgPath = os.path.join(signalImgDir, f"{folder}_{os.path.basename(image)}")
                    cv2.imwrite(outputImgPath, signalArea)

                    # 신호 정보 저장
                    outputTextPath = os.path.join(signalTextDir, f"{folder}_{os.path.basename(image)}.txt")
                    with open(outputTextPath, 'w') as txt_file:
                        txt_file.write(f"{signInfo}")
def main() :
    # 데이터 나누기 및 저
    imageConvert()

if __name__ == '__main__' :
    main()