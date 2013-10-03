pyLapse
=======

Python Timelapse Image Creator using pyGame

##Usage

```shell
timelapse.py -t <lapsetime> -p <path>
```

Additionally, the dimensions of the image you want to create can be passed to this program can be specified.
If the camera supports the size specified then the images will be created at that size, otherwise they will be generated
at a size the camera supports. The below example will take a picture every 60 seconds, store images in the directory `/path/to/store/images/` and attempt to create images that are 1024 pixels by 768 pixels.

```shell
timelapse.py -t 60 -p /path/to/store/images -d 1024x768
```
