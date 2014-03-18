library(ROSE)
data = read.csv("C:/Users/Preeti/Documents/GitHub/research-data/Data/Jacob/StackOverflow/full_data/questionsCompleteData.csv")
data.att = data[,c(1,2,3,4,5,6,7)]
#summary(first.data)

#new.first.data = SMOTE(first$FirstPronoun ~ ., data, perc.over=300,perc.under=50)

alt.first.data = ovun.sample(FirstPronoun ~ ., data.att, N=400000,method="under")
alt.first.data$data = alt.first.data$data[with(alt.first.data$data,order(-alt.first.data$data$Id)),]
write.csv(alt.first.data$data,"C:/Users/Preeti/Documents/GitHub/research-data/Data/Jacob/StackOverflow/full_data/undersampled_first.csv")
pcs_first = prcomp(alt.first.data$data[,c(3,4,5,6,7)])
pairs(pcs_first$x,main="Principal Components: First-Person Pronouns",col=alt.first.data$data$FirstPronoun)

plot(data.att$EarliestElapsedTime,data.att$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Classified by Presence of First Person Pronoun",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=data.att$FirstPronoun)

plot(alt.first.data$EarliestElapsedTime,alt.first.data$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Undersampled, Classified by Presence of First Person Pronoun",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=alt.first.data$FirstPronoun)

data.att = data[,c(1,2,3,4,5,6,8)]
alt.second.data = ovun.sample(SecondPronoun ~ ., data.att, N=50000,method="under")
alt.second.data$data = alt.second.data$data[with(alt.second.data$data,order(-alt.second.data$data$Id)),]
write.csv(alt.second.data$data,"C:/Users/Preeti/Documents/GitHub/research-data/Data/Jacob/StackOverflow/full_data/undersampled_second.csv")
pcs_second = prcomp(alt.second.data$data[,c(3,4,5,6,7)])
pairs(pcs_second$x,main="Principal Components: Second-Person Pronouns",col=alt.second.data$data$SecondPronoun)

plot(data.att$EarliestElapsedTime,data.att$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Classified by Presence of Second Person Pronoun",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=data.att$SecondPronoun)

plot(alt.second.data$EarliestElapsedTime,alt.second.data$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Undersampled, Classified by Presence of Second Person Pronoun",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=alt.second.data$SecondPronoun)

data.att = data[,c(1,2,3,4,5,6,9)]
alt.third.data = ovun.sample(ThirdPronoun ~ ., data.att, N=300000,method="under")
alt.third.data$data = alt.third.data$data[with(alt.third.data$data,order(-alt.third.data$data$Id)),]
write.csv(alt.third.data$data,"C:/Users/Preeti/Documents/GitHub/research-data/Data/Jacob/StackOverflow/full_data/undersampled_third.csv")
pcs_third = prcomp(alt.third.data$data[,c(3,4,5,6,7)])
pairs(pcs_third$x,main="Principal Components: Third-Person Pronouns",col=alt.third.data$data$ThirdPronoun)

plot(data.att$EarliestElapsedTime,data.att$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Classified by Presence of Third Person Pronoun",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=data.att$ThirdPronoun)

plot(alt.third.data$EarliestElapsedTime,alt.third.data$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Undersampled, Classified by Presence of Second Person Pronoun",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=alt.third.data$ThirdPronoun)

data.att = data[,c(1,2,3,4,5,6,11)]
alt.punct.data = ovun.sample(Punctuation ~ ., data.att, N=1700000,method="under")
alt.punct.data$data = alt.punct.data$data[with(alt.punct.data$data,order(-alt.punct.data$data$Id)),]
write.csv(alt.punct.data$data,"C:/Users/Preeti/Documents/GitHub/research-data/Data/Jacob/StackOverflow/full_data/undersampled_punct.csv")
pcs_punct = prcomp(alt.punct.data$data[,c(3,4,5,6,7)])
pairs(pcs_punct$x,main="Principal Components: Punctuation",col=alt.punct.data$data$Punctuation)

plot(data.att$EarliestElapsedTime,data.att$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Classified by Presence of Punctuation",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=data.att$Punctuation)

plot(alt.punct.data$EarliestElapsedTime,alt.punct.data$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Undersampled, Classified by Presence of Punctuation",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=alt.punct.data$Punctuation)

data.att = data[,c(1,2,3,4,5,6,12)]
alt.negation.data = ovun.sample(Negation ~ ., data.att, N=400000,method="under")
alt.negation.data$data = alt.negation.data$data[with(alt.negation.data$data,order(-alt.negation.data$data$Id)),]
write.csv(alt.negation.data$data,"C:/Users/Preeti/Documents/GitHub/research-data/Data/Jacob/StackOverflow/full_data/undersampled_negation.csv")
pcs_neg = prcomp(alt.negation.data$data[,c(3,4,5,6,7)])
pairs(pcs_neg$x,main="Principal Components: Negation",col=alt.negation.data$data$Negation)

plot(data.att$EarilestElapsedTime,data.att$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Classified by Presence of Negation",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=data.att$Negation)

plot(alt.negation.data$EarliestElapsedTime,alt.negation.data$AcceptedElapsedTime,main="Accepted Elapsed Time vs. Earliest Elapsed Time, Undersampled, Classified by Presence of Negation",xlab = "Earliest Elapsed Time in Milliseconds", ylab = "Accepted Elapsed Time in Milliseconds", col=alt.negation.data$Negation)
