import os

from imageai.Classification import ImageClassification

execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
# prediction.setModelTypeAsDenseNet121()
# prediction.setModelPath(os.path.join(execution_path, "densenet121-a639ec97.pth"))
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2-b0353104.pth"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(
    os.path.join(execution_path, "batoul.jpg"), result_count=5
)
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)


# https://github.com/OlafenwaMoses/ImageAI
# https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Classification
