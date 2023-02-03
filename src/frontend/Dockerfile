# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /app

# install app dependencies
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install 

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH
COPY . .

# RUN npm run dev 

# Compile webpack
# Commented out because the build time takes so long Just use precommit hooks to build
# RUN npm run dev