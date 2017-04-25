setwd("H:\\Naturwissenschaften\\Python\\DB_Project\\Python_Db")

val = getwd()

write(val, file = "genData\\testdata.txt")

data = read.table("genData\\testdata.txt")


jpeg('rtestplot.jpeg')
plt <- plot(data)
invisible(dev.off())
