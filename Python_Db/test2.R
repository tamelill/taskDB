setwd("H:/Python_Db")

data <- read.table("data.txt",sep=",",head=TRUE)
name <- levels(data$Name)
hits <- c(1:length(name))
hitters.frame <- data.frame(name,hits)

hitters.frame


for (element in name){
  anztask <- data$Name == element
  
  hitters.frame$hits[hitters.frame$name == element] <- sum(anztask)
}


mybars <- barplot(hitters.frame$hits,names.arg =hitters.frame$name)
jpeg('rplot.jpg')

#return stdout
hitters.frame


