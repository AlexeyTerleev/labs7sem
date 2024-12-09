from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "spolivin/lang-recogn-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)


def neural_predict_language(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_language = torch.argmax(logits, dim=1).item()
    if predicted_language == 3:
        return 'English'
    elif predicted_language == 12:
        return 'Russian'
    else:
        return predicted_language