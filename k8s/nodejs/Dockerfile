#step 1 : Base Image
FROM node:16.20.0

# Step 2 : Package install
RUN apt -y update; apt -y upgrade; apt -y install vim git net-tools

# Step 3 : Specify working directory
WORKDIR /root

# Step 4 : Config file copy
COPY .bashrc .
COPY .exrc .
COPY hello.js .

# Step 5 : Install express
RUN npm init -y
RUN npm install express
RUN npm install -g nodemon

# Step 6 : Open port
EXPOSE 8000

# Step 7 : Execution program
CMD ["node", "hello.js"]
