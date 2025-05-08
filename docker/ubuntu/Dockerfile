#Step1 : Base images
FROM ubuntu

#Step2 : Install program
RUN apt -y update; apt -y upgrade; apt -y install -q nginx; apt -y install vim

#Step3 : File copy
COPY index.html /var/www/html

#Step4 : Start nginx
CMD ["nginx","-g","daemon off;"]
