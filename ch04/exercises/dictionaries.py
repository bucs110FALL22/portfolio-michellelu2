article = '''The Toronto Blue Jays and New York Yankees have had a strong rivalry for decades. Yankees television play-by-play man Michael Kay added some fuel to the fire with a playful jab at Blue Jays star Vladimir Guerrero Jr. after New York clinched the AL East title with a 5-2 win over Toronto on Tuesday at Rogers Centre. "It's really nice of Vlad Guerrero to let the Yankees celebrate in his house. Congratulations to the Yanks," Kay said on the YES Network broadcast. The line was poking fun at Guerrero Jr. for his celebration after his walk-off single in Monday's dramatic 3-2 win in 10 innings. Cameras caught Guerrero Jr. saying 'My house' after driving in Cavan Biggio in the series opener, delighting the crowd at Rogers Centre. The teams wrap up the series on Wednesday -- and it's possible the AL East rivals could meet again later in the playoffs.'''

substitutions = {
  "Blue":"Red",
  "rivalry":"friendship",
  "decades":"only 3 months",
  "YES":"Not Sure",
  "dramatic":"anticlimatic",
  "later":"in 20 years",
  "really":"kinda",
  "win":"epic victory"
}

for key, value in substitutions.items():
  article = article.replace(key,value)

print (article)