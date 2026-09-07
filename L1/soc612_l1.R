### SOC612: Data Analytics for the Social Sciences
### Date: September 8, 2026
### Author: Raphi Duerr
### Lecture 1: Introduction

# Hello World!

# This is a raw R script. Let's test a few commands to see if everything runs
# correctly:

2+8
2==8
2>8 | 2<8
2>8 & 2<8
sqrt(81)

# If everything is ok so far, let's do a few more:

v <- 1:10
x <- 91:100
w <- c("HK","NT","KLN")

class(v)
class(w)
length(v)
levels(w)

a <- x + v
b <- x * v
c <- x - v
d <- v/3

data <- cbind(a,b,c,d)

# Final test! Let's see if we can install a package:

install.packages("tidyverse")
library(tidyverse)

