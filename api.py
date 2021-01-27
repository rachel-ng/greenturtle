import requests
import json

def main():
    PARAMS = {'data':'https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg'}
    #endpoint = 'https://localhost:5000/predict'
    endpoint = 'https://greenturtle.herokuapp.com/predict'
    response = requests.post(url=endpoint, data=PARAMS, verify=False)
    print(response)
    print(response.text)
    print(type(response.text))
    print(type(response))

if __name__ == "__main__":
    main()

