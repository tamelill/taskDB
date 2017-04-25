

data <- read.table("data.txt",sep=",",head=TRUE)
name <- levels(data$Name)
hits <- c(1:length(name))
hitters.frame <- data.frame(name,hits)



for (element in name){
  anztask <- data$Name == element
  
  hitters.frame$hits[hitters.frame$name == element] <- sum(anztask)
}

jpeg('rplot.jpeg')
plt <- barplot(hitters.frame$hits,names.arg =hitters.frame$name)
invisible(dev.off())


#return stdout
hitters.frame
