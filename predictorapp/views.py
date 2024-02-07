from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import numpy as np
from .models import Cotton,Tomato,Potato
# import cv2





# Create your views here.


def homepage(request):
    
    
    return render(request,"college.html")


def signin(request):
    message=""
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST['password']
        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            print("hello")
            print(request.user)
            message="able to login"
            return HttpResponseRedirect("/predictor/")   
            
        else:
            message="not able"    
        
    
    return render(request,"signin.html",{"message":message})
    
    
    # return render(request,"signin.html")




def signup(request):
    message=""
    if request.method=="POST":
        
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        # profilepicture=request.FILES['profilepicture']
        
        if name=="" or email=="" or password==""  or password1=="":
            message="field is empty"
            print("Field is empty")
            
        elif len(password)<8:
            print("Password should be grater than the 8")
            message="password should contain 8 character"
        
        elif password!=password1:
            message="Both the password should be same"    
        
        elif User.objects.filter(email=email).exists():
            message="Your email is already present"
        
        elif User.objects.filter(username=name).exists():
            message="Your username is already present"    
        
        elif email=="" or password==""  or password1=="":
            print("Field is empty")
            
        
        else:
            User.objects.create_user(name,email,password)
            user = authenticate(username=name,password=password)
            login(request, user)
            # pp=User.objects.get(username=name)
            # Profilepicture(profilepicture=profilepicture,username=pp).save()
            print(request.user)
            
            message="you can loggin"
            print("Able to login")
            return HttpResponseRedirect("/predictor/")    
            
   
        
    return render(request,"signup.html",{"message":message})
    
    # return render(request,'signup.html')
    
    





@login_required
def predictor(request):
    message=""
    if request.method=="POST":
        plantname=request.POST['plantname']
        plantimage=request.FILES['plantimage']
        # print(img)
        fs = FileSystemStorage()
        filename = fs.save(plantimage.name, plantimage)
        image_path = fs.path(filename)
        image=load_img(image_path)
        
        
        
        if plantname=="cotton":
            image=image.resize((200,200))
            imgarray=img_to_array(image)
        
     
            normalizeimage=imgarray/255
            finalimage=tf.expand_dims(normalizeimage,axis=0)
            # Cotton(cotton=plantimage).save()
            
            class_names=['diseased cotton leaf', 'diseased cotton plant', 'fresh cotton leaf', 'fresh cotton plant']
            model=load_model("/Users/khumapokharel/Desktop/geekyshowsagiserver/FinalCollegeProject/predictor/model/cotton.h5")
            result=np.argmax(model.predict(finalimage))
            # print(class_names[result])
            message=class_names[result]
            
            
            # print("cotton")
            
        if plantname=="tomato":
            image=image.resize((256,256))
            imgarray=img_to_array(image)
        
     
            normalizeimage=imgarray/255
            finalimage=tf.expand_dims(normalizeimage,axis=0)
            
            
            class_names=['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy']
            model=load_model("/Users/khumapokharel/Desktop/geekyshowsagiserver/FinalCollegeProject/predictor/model/tomato.h5")
            result=np.argmax(model.predict(finalimage))
            # print(class_names[result])
            # print("tomato")
            message=class_names[result]
            
            
            
        if plantname=="potato":
            image=image.resize((256,256))
            imgarray=img_to_array(image)
            normalizeimage=imgarray/255
            finalimage=tf.expand_dims(normalizeimage,axis=0)
            
            class_names=['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
            import h5py

# Open the HDF5 file in read-only mode
            # f = h5py.File("/Users/khumapokharel/Desktop/geekyshowsagiserver/FinalCollegeProject/predictor/model/potato.h5", "r")
            model=load_model("/Users/khumapokharel/Desktop/geekyshowsagiserver/FinalCollegeProject/predictor/model/potato.h5")
            result=np.argmax(model.predict(finalimage))
            # print(class_names[result])
            message=class_names[result]
            
            
            
            # print("potato")
            
    
    
    
    
    return render(request,"leaf.html",{"message":message})

