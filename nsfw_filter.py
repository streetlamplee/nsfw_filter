from transformers import pipeline
from PIL import Image

class Nsfw_filter:
    model = None
    def load_model():
        """서버 시작 시 모델을 로드합니다."""
        global classifier
        print("Loading AI Model... (This may take a while for the first time)")
        try:
            # 모델은 docker-compose에 정의된 볼륨 경로에 저장됩니다.
            classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
            print("Model loaded successfully!")
        except Exception as e:
            print(f"Failed to load model: {e}")


    def predict_image(image:Image):
        if classifier is None:
            raise Exception("Model is not ready yet.")

        # 추론 수행
        results = classifier(image)
        
        return results