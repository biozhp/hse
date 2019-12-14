## The following codes run under R

## Pearson's Chi-squared test (Line 205)
grain <- matrix(c(33,75,339,935,5741,16567),nrow=3,ncol=2)
chisq.test(grain,correct=FALSE)
leaves <- matrix(c(108,301,1212,860,5515,15694),nrow=3,ncol=2)
chisq.test(leaves,correct=FALSE)

## Multivariate analysis of variance (MANOVA) (Line 212)
data <- read.table("./example/manova/TTG_HS_grain.txt",header=T,sep="\t")
head(data)
x <- factor(data$response)
y <- cbind(data$pos,data$subunit)
fit <- manova(y~x)
summary(fit)
summary.aov(fit)
## The other input files are in the folder ("./example/manova/"), run with the same codes.

## One-way analysis of variance (ANOVA) (Line 228)
data <- read.table("./example/anova/Grain_MFH.txt",header=T,sep="\t")
y <- scale(data$MFH,scale=T,center=T)
x <- data$type
fit <- aov(y~x)
summary(fit)
## The other input files are in the folder ("./example/anova/"), run with the same codes.

## One-way analysis of covariance (ANCOVA) (Line 235)
data <- read.table("./example/ancova/Grain_MFH_T.txt",header=T,sep="\t")
x <- data$position
y <- scale(data$MFH,scale=T,center=T)
c <- data$subunit
fit <- aov(y~c+x) ### c is a covariate.
summary(fit)
## The other input files are in the folder ("./example/ancova/"), run with the same codes.

## Pearson's product-moment correlation (Line 235)
data <- read.table("./example/ancova/Grain_MFH_V.txt",header=T,sep="\t")
x <- data$position
y <- scale(data$MFH,scale=T,center=T)
cor.test(x,y)
data <- read.table("./example/ancova/Leaves_MFH_G.txt",header=T,sep="\t")
x <- data$position
y <- scale(data$MFH,scale=T,center=T)
cor.test(x,y)
data <- read.table("./example/ancova/Leaves_MFH_V.txt",header=T,sep="\t")
x <- data$position
y <- scale(data$MFH,scale=T,center=T)
cor.test(x,y)

## Multiple comparison analysis (Line 238)
library(multcomp)
data <- read.table("./example/mca/Leaves_MFH_V_nor.txt",sep="\t",header=T)
fit <- aov(normalized_MFH~subunit+position,data=data)
par(mar=c(5,4,6,2))
tuk <- glht(fit,linfct=mcp(subunit="Tukey"))
plot(cld(tuk,level=.05),col="lightgrey")

## One-way analysis of covariance (ANCOVA) (Line 249)
data <- read.table("./example/base/Grain_TVGs_G.txt",header=T,sep="\t")
x <- data$base
y <- scale(data$MFH,scale=T,center=T)
c <- data$pos
fit <- aov(y~c+x) ### c is a covariate.
summary(fit)
## The other input files are in the folder ("./example/base/"), run with the same codes.

## Multiple comparison analysis (Line 262)
library(multcomp)
data <- read.table("./example/base/Grain_TGGs_G.txt",sep="\t",header=T)
nor <- scale(data$MFH,scale=T,center=T)
fit <- aov(nor~base,data=data)
par(mar=c(5,4,6,2))
tuk <- glht(fit,linfct=mcp(base="Tukey"))
plot(cld(tuk,level=.05),col="lightgrey")
summary(fit)
data <- read.table("./example/base/Grain_TVGs_22_G.txt",sep="\t",header=T)
nor <- scale(data$MFH,scale=T,center=T)
fit <- aov(nor~pos+base,data=data)
par(mar=c(5,4,6,2))
tuk <- glht(fit,linfct=mcp(base="Tukey"))
plot(cld(tuk,level=.05),col="lightgrey")
summary(fit)
data <- read.table("./example/base/Grain_TVGs_23_G.txt",sep="\t",header=T)
nor <- scale(data$MFH,scale=T,center=T)
fit <- aov(nor~pos+base,data=data)
par(mar=c(5,4,6,2))
tuk <- glht(fit,linfct=mcp(base="Tukey"))
plot(cld(tuk,level=.05),col="lightgrey")
summary(fit)
data <- read.table("./example/base/Leaves_TVGs_12_C.txt",sep="\t",header=T)
nor <- scale(data$MFH,scale=T,center=T)
fit <- aov(nor~pos+base,data=data)
par(mar=c(5,4,6,2))
tuk <- glht(fit,linfct=mcp(base="Tukey"))
plot(cld(tuk,level=.05),col="lightgrey")
summary(fit)