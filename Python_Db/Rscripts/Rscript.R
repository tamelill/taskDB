#setwd("H:\\Naturwissenschaften\\Python\\DB_Project\\Python_Db")


data <- read.table("genData\\data.txt",sep=";",head=TRUE)

name <- levels(data$Name)
hits <- c(1:length(name))
hitters.frame <- data.frame(name,hits)



for (element in name){
  anztask <- data$Name == element

  hitters.frame$hits[hitters.frame$name == element] <- sum(anztask)
}

jpeg('Plots\\rplot.jpeg')
plt <- barplot(hitters.frame$hits,names.arg =hitters.frame$name)
invisible(dev.off())


#return stdout
hitters.frame

