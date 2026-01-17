# 5 Class 5 - Inside Bitcoin: Mining, Halving and the Cycles

## :movie_camera: Class Video

[![Watch Video](https://img.youtube.com/vi/Fw56Z332YAg/maxresdefault.jpg)](https://www.youtube.com/watch?v=Fw56Z332YAg)

:point_right: **[Click here to watch on YouTube](https://www.youtube.com/watch?v=Fw56Z332YAg)**

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://www.youtube.com/embed/Fw56Z332YAg?rel=0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;border-radius:12px;" title="Video"></iframe></div>

---
---

##  Full Script

# Script Class 5 - Inside Bitcoin: How Does Bitcoin Work? (mining, halving and the cycles)

![Slide 108](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-01.jpg)

Now that you've understood how the Bitcoin blockchain works and that it needs consensus from participants for decentralized coordination to exist, let's understand how the network agrees with itself through the mechanism called Proof of Work (PoW).


![Slide 109](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-02.jpg)

Bitcoin mining is an analogy for the process of searching for something precious, like gold, but in the Bitcoin network this precious something is the hash of each block. In gold, miners keep digging the deposit until they find the precious metal, when they find it, they have something scarce and valuable in hand. Gold is scarce and over time it becomes more difficult and more expensive to mine gold, because you have to dig deeper into the ground. It requires increasingly modern and efficient equipment to access the deeper and more complex deposits.

With Bitcoin something very similar happens. In the bitcoin network, miners compete with each other, through trial and error, to see who arrives first at the hash that closes each block of information.

![Slide 110](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-03.jpg)

Remember that the block is made up of several components? The hash of the previous block, a date and time stamp called timestamp and all the transaction data?

Along with this information there is also a piece of data called "nonce". Nonce means "number used only once". When miners use computational power to mine the block it means they are, at an absurd computational speed, trying to find this number that can only be used once by the network. It is this number that all miners are competing to find.

In the block header goes the hash that mixes all these components: the hash of the previous block, the timestamp, the root transaction that summarizes all the transactions that entered the block and the nonce.


![Slide 111](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-04.jpg)

Everyone is looking for the correct piece among all possibilities and whoever finds it first tries to fit it into the image. When the miner finds the missing piece, it's very easy for everyone to notice if it fit. Just look at the image and see if the piece was correct or not.

This means that mining is a process that is difficult to defraud and at the same time very easy to verify. Just as it is hard to find the correct piece in a giant puzzle, but it is easy to verify if it was the missing piece or not. Bitcoin is like a global puzzle where the whole world participates and follows the results in real time.


![Slide 112](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-05.jpg)

The entire mining and consensus process when recording the Bitcoin blockchain works like this:

Miners employ computational power, buying powerful machines with great computational power to try to find the block's nonce as fast as possible. When they find it, they create the hash, show it to the network, and the nodes verify if the proposed block is following the rules. If everything is ok, this block is inserted into the chain of blocks, propagated through the network and all participants insert this block in their copies of the blockchain. And in the end, miners receive Bitcoin as a reward for completing the task.

This whole process is known as proof of work.


![Slide 113](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-06.jpg)

Proof of work means that the miner found the nonce, created the block's hash, followed the rules and provided a computational service to the network. When all the block's information is found, it goes through the cryptography process, transforming the information into a cryptographic puzzle using SHA-256. The result is that huge number below, which represents the block's hash, the result of all the miner's work.


![Slide 114](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-07.jpg)

This process is not exclusive to Bitcoin, but to anything that can be encrypted, and SHA-256 is the algorithm that does this. SHA-256 takes information of any size and creates a sequence of 256 bits: a series of 256 zeros and ones. From this huge number full of 01010101 the algorithm creates a hexadecimal sequence made up of 64 digits between letters and numbers that is easier to write down. That is, it is easy to verify if it is correct, but it is practically impossible to forge the information that was encrypted.

Trying to randomly guess a hash and break SHA-256 encryption is practically impossible. It involves an absurdly high number of possible combinations, more numbers than the amount of atoms in the observable universe! This would require a number of attempts so large, but so large, that a normal computer would take billions of years to accomplish this.

This is where the quantum computer story comes in! People always ask us if a quantum computer could break Bitcoin's cryptography. This is one of the great hopes of Bitcoin haters, but the truth is that probably no quantum computer could kill Bitcoin.

Below this class I'll leave an [article](https://blog.areabitcoin.com.br/computadores-quanticos-podem-destruir-o-bitcoin/) that explains this.

I want to show you a very cool [website](https://codebeautify.org/sha256-hash-generator). It's called code beautify. This site allows you to experiment and convert any information into a SHA-256 function.

I'm going to type Bitcoin4All here and watch how the code in the box below changes with each letter, space or punctuation inserted. This is what happens with the hash of the block on the Bitcoin network if any information is modified. Also notice how fast it was, it didn't require mega computational power to find this hash. So if it was so easy to create a hash here on this site, why does it take 10 minutes on the Bitcoin network and is it no longer possible to mine from a home computer?


![Slide 115](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-08.jpg)

This has to do with a mechanism called difficulty adjustment.

The difficulty adjustment has the role of regulating the issuance of new Bitcoin. It is this adjustment that ensures that the average creation of new blocks and the reward delivered by the network is 10 minutes. This is because every 2016 blocks mined, about 15 days on average, there is an algorithm that will analyze the amount of computational power on the network and increase or decrease the difficulty of finding the block's hash.

If suddenly the number of miners increases a lot, the network will self-regulate to increase the mining difficulty so as not to accelerate the speed at which new blocks are created and consequently not accelerate the speed at which new Bitcoin is created.


![Slide 116](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-09.jpg)

It works like this: as more miners join the network and the hashrate increases (the rate of new block creation), miners start finding blocks more easily and the average mining time between one block and another gets faster. The network notices this through algorithms and increases mining difficulty, with this the speed of creation of new blocks drops, because it became harder for miners to find blocks, until it stabilizes at the average of 10 minutes between one block and another.

This is how the network self-regulates with increased demand to never lose its predictability.


![Slide 117](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-10.jpg)

You can tell the difficulty level of mining each block according to the number of zeros that appear before the block's hash number. This block for example has 24 zeros in front of the hash code, was mined in October 2022 and is one of the blocks that had the most difficulty being mined at the time.

The miner's goal is to assemble a block where the hash code is less than the current target (second to last blank line). The lower the target, the harder it is to find a valid block. The more miners on the network, the harder it gets.


![Slide 118](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-11.jpg)

In other words, the more zeros leading a hash, the harder to mine, the more the miner had to keep searching for the block's nonce until finding it.


![Slide 119](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-12.jpg)

It is because of the difficulty adjustment that mining evolved and it is no longer so easy to mine from a home PC, from a CPU. Today bitcoin mining is done with specific machines called ASICs. As the price of Bitcoin went up, it ended up attracting more and more people, more computational power was being employed in the network and with this the difficulty adjustment algorithm was increasing to maintain the average of one block mined every 10 minutes.

With the increase in difficulty, the more tech-savvy people started using more powerful machines: GPUs, widely used in gaming computers. Bitcoin continued to attract more and more people wanting to mine, until they decided to create a specific machine: ASICs.

This type of machine is much more powerful and beats CPUs and GPUs in the speed of finding the block's hash. Mining has become a giant and dedicated industry, which tirelessly seeks efficiency. That is, producing the maximum Bitcoin with the minimum energy or with cheap energy.

That's why the price doesn't matter. Bitcoin can go to 10 billion dollars. The speed of issuance of new bitcoin doesn't change. Even the increase in hashrate power cannot lead to the issuance of more Bitcoin beyond what is planned for each halving cycle. The entry of more miners into the network does not produce more bitcoin, but makes the network more secure and decentralized.


![Slide 120](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-13.jpg)

And why does this mechanism make the network more secure? This happens because the greater the computational power, the harder it is to attack the network. In this graph the line represents the hashrate, the computational power, and the more reddish colors represent the difficulty of mining each block. Difficulty and hashrate have been increasing exponentially since bitcoin started running. As the line turns orange, the greater the difficulty of mining a block. The greater the computational power, the more the network has adapted to protect Bitcoin's properties. That's why Bitcoin has no competitor in mining, it is the protocol with the most distributed miners around the planet and with the greatest computational power of all.


![Slide 121](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-14.jpg)

Bitcoin is 631 times more powerful than the 500 largest supercomputers in the world combined, represented in the white line, and Bitcoin is shown in the orange line. Bitcoin has the most attack-resistant computational network and 600x stronger than any centralized computational system or data center.

But the advancement of mining didn't stop at ASICs. Over time, even having a super powerful machine, it became increasingly difficult to find blocks and miners ended up grouping into pools. They pool their computational power to have more chances of finding blocks and sharing the reward.


![Slide 122](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-15.jpg)

Mining pools work between the Bitcoin software and the miners, allowing miners to pool the computational power of their machines and have more chances of finding a block. Pool comes from the word pool, a concentrated grouping of computational power.


![Slide 123](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-16.jpg)

To give you an idea of how difficult it is to mine outside a pool, that is, to mine solo, an S19JPRO which is one of the most modern ASIC machines, has a 0.000000208% chance of mining a Bitcoin block. This means one chance in almost 4.8 billion attempts throughout the machine's useful life, which lasts on average 5 to 8 years. This probability will continue to decrease over time, as more miners arrive, the hashrate rises and the difficulty increases.


![Slide 124](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-17.jpg)

That's why pools are like a pooling of computational power, when someone finds the block everyone splits the Bitcoin reward proportionally to each one's hash power. This way, miners can have frequent revenue instead of waiting for the luck of finding a block on their own, which can take years and still without any guarantee of happening.


![Slide 125](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-18.jpg)

Today the Bitcoin network has dozens of pools, but five of them are the largest and aggregate most of the hashrate: Foundry, Antpool, F2Pool, ViaBTC and Mara. Although many people say this would be a centralization mechanism, in fact miners can leave the pool at any time and go to another, or they can even mine solo if they want to try their luck. That is, the concentration in these five largest pools was a natural market movement of the miners themselves wanting to be in the pools with the highest probability of finding blocks and sharing the rewards. The pools don't control the network, even because it is the nodes that verify and decide if the mined blocks are valid or not.

And the last extremely important point in how Bitcoin works are the halvings, which have everything to do with mining. As time passes, Bitcoin becomes increasingly scarce. Growing scarcity combined with growing demand is what has caused parabolic price increases in Bitcoin. It is the halving that makes Bitcoin gradually become more scarce and at the same time create valuation cycles that have been repeating.


![Slide 126](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-19.jpg)

Halving comes from the word "halving" and means "to cut in half". It means that every 210 thousand blocks mined, on average every 4 years, the protocol cuts the reward delivered to miners in half.


![Slide 127](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-20.jpg)

The first halving happened on November 28, 2012, right at the beginning of the network. At the time, the Bitcoin network produced 50 bitcoin per block of information processed. That is, every 10 minutes, on average, at that time, miners received 50 btc as a reward. With the 2012 halving, miners started receiving 25 bitcoin per mined block.

In 2016 the second halving happened, at block 420 thousand, and again cut the issuance in half. Instead of receiving 25 bitcoin per block, each miner started receiving 12.5 bitcoin per mined block. And the third halving happened in 2020, on May 11, at block 630 thousand, where miners started receiving 6.25 btc per block.

The last recorded halving, the fourth, happened in April 2024 at block height 840 thousand. The next one will be in 2028. And the cool thing about all this is that we know in advance at what block it will be, at block height one million and fifty thousand. The new reward will become 1.5625 bitcoin for miners.


![Slide 128](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-21.jpg)

This image demonstrates how with each step of the orange line, that is with each halving, Bitcoin slowly becomes more scarce and approaches the unit supply limit, in the blue line.

This image is incredible, because it shows how Bitcoin is transparent, programmable and has a predictable monetary policy that cannot be expanded or modified. It is something very different from any other asset or currency that changes rules or monetary policies at any time.

The last satoshi will be mined in the year 2140 and that's when the issuance of new bitcoin ends. Only network fees will be the source of revenue for miners to pay operating costs.


![Slide 129](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-22.jpg)

And this table here is another way of showing the same thing. This table shows Bitcoin's entire monetary policy, from the first satoshi, the first halving to the last halving in 2140.

This table shows that more than 90% of Bitcoin has already been issued and that, by the year 2036, 99% of bitcoin will be mined. The rest, the other final 1% will be created from 2036 to 2140. That's 110 years to mine 1% of the bitcoin supply!

In the year 2030 is when, probably, the biggest source of revenue for miners becomes fees. At this moment, the demand for Bitcoin should be very large, to the point where the fees charged by miners sustain their operation, including machine maintenance and energy costs, and not so much the block reward anymore.


![Slide 130](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-23.jpg)

When we talk about 2140 comes the fear of the unknown and the doubt: "what happens when the last bitcoin is mined?"

The answer is: nothing. This big change starts much earlier. Already in 2030 fees tend to be the main source of revenue for miners. When it reaches 2140 miners will probably be receiving much more in fees than the few satoshis offered by the network, because of the growing increase in the scarcity of the currency, increase in fiat price and increase in network usage.

And why is the halving so important?


![Slide 131](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-24.jpg)

The halvings create a "supply shock": fewer Bitcoins become available while demand remains the same. With each halving, the amount of Bitcoins created per block is cut in half. This reduces supply, which makes the price go up. If many people want to buy Bitcoin and you can't create more units, the only way to convince hodlers to sell is by offering a higher price.


![Slide 132](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-25.jpg)

Hodlers are bitcoiners who accumulate bitcoin for the long term and don't sell even during the biggest short-term drops. The term hodler became a meme because a guy on bitcoin talk, a famous bitcoin forum, typed it wrong and people adopted the slang to differentiate from the traditional stock market crowd. This image on screen is the print of the post that gave name to the hodlers: bitcoiners who hold bitcoin tight and don't sell no matter what.

This rise forms parabolic movements, catches everyone's attention, Bitcoin appears in the news and increases demand even more. And that's when the frantic euphoria of the bull run begins.

This happens because the only way to have the same liquidity to satisfy new buyers is by increasing the premium so that those who have Bitcoin change their minds and want to sell. It's the simplest law of economics: the law of supply and demand. If there is a lot of demand and supply decreases, prices go up. Since the number of Bitcoin is limited to 21 million units and there's no way to issue more, when demand increases, the only way for supply to meet demand is for the price to go up.

The halvings cause supply shocks that make bitcoin rise until a new price discovery. This whole process creates cyclical movements of appreciation and contraction until the new price is defined.


![Slide 133](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-26.jpg)

Bitcoin cycles are formed by four phases. The first phase is the BEAR, when the market belongs to the bears. It's when the price drops a lot after a period of highs and it's when those who entered during the highs leave. 2011, 2014, 2018 and 2022 were Bitcoin bear years. It's when only negative news comes out and those who were just tourists in Bitcoin leave.

After the bear comes a VERY agonizing phase, which is the accumulation phase. It's when bitcoin moves sideways for an entire year. Nothing happens, it's pure boredom and it seems like it will never end.

The next phase is the expansion or growth phase. When bitcoin starts to rise slowly, as if not wanting anything. It's the phase where haters attack because they don't believe in a new rise and bitcoiners begin to renew hopes that a new bull run is approaching. 2012, 2016, 2020 and 2024 were expansion years.

And lastly comes the bull run, the bull stampede. When bitcoin reaches the cycle's peak and runs like an unbridled bull without anything being able to hold it back. This phase is all joy, euphoria and the haters disappear! Bitcoin is on everyone's lips, draws attention and reaches a new price level. When the euphoria passes, comes the drop and a new price floor is established, and so everything goes back to the beginning, to the bear phase. It's a mental and emotional roller coaster.


![Slide 134](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-27.jpg)

So much so that to measure the emotional state of the market, the fear and greed index was created. Where the closer to 0 means "Extreme Fear", and the closer to 100 represents "Extreme Greed".


![Slide 135](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-28.jpg)

People generally want Bitcoin to appreciate in a straight line, but the biggest rises took a year to reach the peak of the movement. Here I zoomed in so we can analyze Bitcoin's price in the halvings. From the halving to the cycle top it has taken about a year to hit ATH (all time high), but this doesn't happen in a straight line, the chart fluctuates a lot, but with an ascending average of appreciation. Bitcoin appreciated 11 thousand percent after the first halving, 2,500 percent after the second halving and a thousand percent after the third halving in 2020, when it reached the last ATH at 69 thousand dollars. In 2024 the fourth halving happened, Bitcoin has already hit $100k and whoever lives will see how far the price can go in this cycle.


![Slide 136](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-29.jpg)

But everything that goes up also comes down. Bitcoin despite having had large appreciations and them having decreased in intensity over the years, the same has happened with the drops.

In 2012 Bitcoin had a brutal drop of 93%, after the first halving 84%, in the second it dropped 84% again and in the last halving the drop was 77%, smaller than in previous bears. This means that over time bitcoin is becoming less volatile. Obviously it's far from moving in a straight line, but this trend can already be observed.


![Slide 137](https://raw.githubusercontent.com/areabitcoin/Bitcoin-4-All/d04005ed63f756f0a60807071eb6a303b56c8080/Bitcoin%204%20All%20-%20Portuguese/Slides/AULA%205/Sem%20ti%CC%81tulo-12-30.jpg)

What is also observed is that Bitcoin has had increasingly higher lows over the cycles. In 2012 bitcoin was worth less than a dollar, in 2014 the low was already ten dollars, in 2016 one hundred dollars, in 2019 a thousand dollars and in 2022 ten thousand dollars.

That is, no matter how much Bitcoin drops, it has maintained increasingly higher minimum prices over time. But will it always be like this? Will Bitcoin continue to appreciate forever?

That is the subject of the next class. Now that you've learned how bitcoin works and Bitcoin's cycle history, it's time for you to understand why it tends to continue growing in the long term. See you there.

---

### :loudspeaker: Share this lesson!

<div class="share-buttons">
<a href="https://twitter.com/intent/tweet?text=I'm%20learning%20about%20Bitcoin!%20Class%205%20from%20Bitcoin%204%20All%20course%20&url=https://areabitcoin.github.io/Bitcoin-4-All/en/class-5&via=aaborges_" target="_blank" class="share-btn share-btn-twitter">
 Twitter
</a>
<a href="https://www.linkedin.com/sharing/share-offsite/?url=https://areabitcoin.github.io/Bitcoin-4-All/en/class-5" target="_blank" class="share-btn share-btn-linkedin">
 LinkedIn
</a>
<a href="https://wa.me/?text=I'm%20learning%20about%20Bitcoin!%20Class%205%20from%20Bitcoin%204%20All%20course%20%20https://areabitcoin.github.io/Bitcoin-4-All/en/class-5" target="_blank" class="share-btn share-btn-whatsapp">
 WhatsApp
</a>
<a href="https://t.me/share/url?url=https://areabitcoin.github.io/Bitcoin-4-All/en/class-5&text=I'm%20learning%20about%20Bitcoin!%20Class%205%20from%20Bitcoin%204%20All%20course%20" target="_blank" class="share-btn share-btn-telegram">
 Telegram
</a>
</div>

### :chart_with_upwards_trend: Your Course Progress

<div class="course-progress">
<strong>Class 5 de 10</strong> (50% completo)
<div class="course-progress-bar">
<div class="course-progress-fill" style="width: 50%"></div>
</div>
</div>
