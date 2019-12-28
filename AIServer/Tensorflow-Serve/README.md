# Tensorflow Serving

Getting into the tensorflow serving ecosystem.

Super easy, they have a well supported docker container, and you just hit that endpoint. 

All models are saved in the /var/lib/osiris/ folder.

As well, they are under specific folders per framework (aka tensorflow-serve, pytorch-serve, etc..)

## Requirements

Docker: https://docs.docker.com/install/linux/docker-ce/ubuntu/
Nvidia-Docker: https://github.com/NVIDIA/nvidia-docker
Docker-Compose: https://docs.docker.com/compose/install/

## Serving Multiple Models

https://www.tensorflow.org/tfx/serving/serving_config

    model_config_list {
        config {
            name: 'my_first_model'
            base_path: '/var/lib/osiris/tensorflow-serve/my_first_model/'
        }
        config {
            name: 'my_second_model'
            base_path: '/var/lib/osiris/tensorflow-serve/my_second_model/'
        }
    }

## Resources

Serving ML Quickly with TensorFlow Serving and Docker: https://medium.com/tensorflow/serving-ml-quickly-with-tensorflow-serving-and-docker-7df7094aa008