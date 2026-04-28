# Transcript
**URL:** https://youtu.be/R6Sf34dIImM

♪ [music] ♪ I am Adam. I work with developer-focused
companies on creating better content, anything that
inspires or educates. But today I am probably best known here
as the guy whose bag was swallowed by a cocktail table and went around
for an hour trying to find it. So, thank you to half of the conference
who helped me finally locate my bag. So, today I'm going to talk about
having a more inclusive developer portal, the people who are already
showing up that you, not on purpose, you're accidentally ignoring. So, first start, I'll start here. Anyone seen this before? So, thumbs up if you see
the plates right side up. Yeah. And thumbs down... Nothing against you, but
thumbs down if you see them the other way. Most people are up. What happens if you scan
these enough, you can switch. There's a moment, if you sort of go corner
to corner where if you were seeing them one way, then you'll
see them the other way. And if you get good enough at it,
and I stared at my slides a bit, then you can do it sort of on command,
you can change the way you see it. And that's what I want you to think about
with the people who are visiting your portal that all of the information is
there and it's just the way you look at it that can change how you see it. And now this is…well, if you
think too much about metal detecting in Second Life and what that
would really mean it's actually a little bit sad to like…so,
don't go too deep into thinking about that. But if you think about metal
detecting, overall, it can be a fun time. My kids enjoy it. And what I noticed is one of
them really likes to find the spot, and then the other one
really likes the digging part. And it didn't occur to me that you
would like one over the other. I thought it was sort of all one
experience, but reminded me of editing Programmable Web, and
some editors like to find new APIs and some like to fill out the 30
items of information that you can can tell which part I didn't like. And I talked to the team and I had
this huge obvious epiphany that people are different. And I think that can help us as we
think about our developer portals also. And so today I'm going to be talking
about rethinking your audience to be able to get the eye control thing in
find out what they want, and then make it easier for
them to get it. And so this piece is probably the biggest
part, the rethinking the audience, and we are hampered by an industry
that perpetuates the idea of the single developer. And even though those of us in this
room are much better than the average, we all probably still have... You know, whether or not it's this, we
all still have our expectation of what our developer that we
are talking to wants. Three years ago, I wrote this, which
was about basically how so many people who are coming to our documentation
and banging their heads against it are not the people we think they are. They're not the developers. They are just someone who knows that this
API or this technical thing can help them solve something and they're
just trying to make it happen. And so after that, I ended up working at
Zapier, which some of you might make a ton of sense because this serves exactly
that audience, connecting APIs together without them having to write code. But I actually worked on the supply
side, the platform, the one that works with developers to be able to connect
their APIs to it or so I thought. And I'll talk about that in a little bit. Zapier is, of course, one of
many of these that even in these last three years have
shown up these low code tools. And this is the context that our
developers or the people who are visiting our portals, this is the
context that they live in now, these other ways of being able to
access our tools and wanting that different experience. But even if you are working with
developers who write code, many many of us are probably
chasing after the same 7 million or so JavaScript programmers. And with the data that's coming out
these days, it's a dangerous language. And I did a search and believe it or not,
there are still people who are hiring Java developers to build and consume SOAP APIs,
and in the time where maybe some of us are so excited about GraphQL
and we're leaving REST behind, there's actually, I mean, people are still using
the technology that we had before that, right? And they may be visiting your portal too. So, you have this huge spectrum that
somewhere in there is who you think it is, but you really need to rethink who
that is, and maybe you need to give them another label. This has stuck with me for a year. I think it was it DevRelCon last
year that Tamao,I believe, talked about operators versus developers
and the label that they used. And maybe that's a way to think about
these different audiences that you have who are visiting you. And the thing is if we don't acknowledge
that there might be someone that we don't see there, then we
will totally miss it. As this is a famous video, I don't
know if any of you have seen this, where you're supposed to track how many
passes the team in white makes with the basketball and while you do there is a
moonwalking bear that walks through the middle and most
people don't see it. And so in your portal, you have
many moonwalking bears and you just need to help
them moonwalk. So, that's what we're going
to find out about today. So, finding out what they want. Yeah. So, this is... I meant to set this up as the most
important point of the talk and get out your journals and write this down
because this is my big takeaway here that you need to do. You need to talk to them. Yeah in a dev rel
conference that's probably not amazing, but there are a lot of ways that you can,
and so I wanted to tell about a way that we at Zapier got information about people
visiting the portal and kind of how we realized that we weren't talking
to who we thought we were. And so shortly before I joined,
we created a new CLI to access the platform, brand new version of the
platform and built the JavaScript apps and do it all from
the command line. And so I helped launch that. And at first we had hundreds of
people on the old visual platform, so we couldn't completely get away with
it, but the first version here we said, "Or you can use the new CLI." So, that's of course what
we wanted them to do. So, thumbs up if you think that
more people use the CLI here. Thumbs down if you think more
people use the visual builder. Yeah, lots of thumbs down. And yeah, and you're right. And that's because there's a
big orange button there, right? So, what happens if we do this? And we put the CLI button on the left
because that's the first thing you'll see. So, now how about a thumbs up they
use the CLI, thumbs down they use the visual builder. There's a few more thumbs up now
but the thumbs downs are right. Yeah, so they still used the builder. And two buttons, we
looked at our style guides. Clearly, we need a primary button. So, we'll do that and that
didn't change anything. This one's... Certainly, this should do it now because
we had that data before we had the one button and then now they
still wanted the visual builder. And these aren't screenshots, but
we put something really close to that and that still did not change the data
that we were seeing because what we realized is the people who
were arriving here were not the developers we thought they were. And that CLI was built by talking
to some of Zapier's best partners, but the best partners didn't necessarily
match the largest group that were coming in wanting to use the platform. And so we ended up using, I think,
pretty much all of these ways. Analytics is kind of what
I was talking about there. But one of the things at some point in
that process, we put a little survey when someone would choose the web builder
and we said, "Why did you do that?" Just a little one question and we
got lots of information out of that. That was how we were able to realize that
what we needed was a new version of the visual builder that would
work on the new platform. And this is actually pretty much what's on
Zapier today now that they launched that. And this looks a lot like that
first version with the…yeah. Use our CLI or use that. Also, switch to Zapier
integration instead of app. So, another part of listening to what the
people at…the words they actually use which there's been plenty
of talk of that here today. This is basically what you need to do as
you're figuring out what people want in their portal is to make sure that
you're listening to the stuff on the right and not getting too buried in the weeds of
what the different wheels and trucks and things are on the skateboard. And even some companies that we think of
as developer companies that have giant billboards that talk about developers,
if you look at the stuff that they are putting out more recently,
it starts to look a little less developery with Flex and
Studio both have this kind of drag-and-drop aspect that I think
speaks to who is trying to use Twilio. And we here know that you can't
always make product changes, but we're really good at making sure
that products gets the feedback that we're hearing. And that's where I think we could
really...the role we can really play. And for many of us, the portal is
something that we control or at least have access to and that's where
we can start to learn from our audience. And the last part, I think we can do a lot
here too is to make it easier for them to get the things that they want. And so this is a bad
portal that I mocked up. The links along the top,
take you to the old docks. You, of course, can
only talk to sales. And when you put your email address in,
it shows up with a blank page for your free API key. But aside from me, nobody makes
bad documentation on purpose. And I wrote a blog post about
this too as I do, and this is it. You can maybe read it later. But it's a list of the reasons that people
do make bad docs accidentally, right? No one is doing it on purpose. But if you're going to look for areas
to improve, again, something we've heard today, get started, helping
someone to get started quickly. And maybe you already have that taken
care of, but now that you've discovered a new audience, you might realize that there
are ways to get them started more quickly. So, you might not have just one getting
started guide, you might have multiple for different use cases. And whether it's a guide or whether it's a
tool, these ways to get people started quickly are really… So, this is... Anyone in dev rel travel ever? Raise your hand. Okay. So, a walkway. And so if you just stand on the
walkway, and it's cool if you do that if you're tired. But if you just stand there, you
eventually get to the destination. But if you walk, then you
get there all the faster. And a couple of those in a row and you
won't miss your connection in London. So, really, what we're doing is we're
creating these different ways to be able to speed people along and to continue to
look for once we know who they are and what they want, how
we can give it to them. There's a lot more in detail
tomorrow afternoon. I know Taylor will talk about getting to
hello world and I think this whole track kind of covers these sort of topics of
getting people maybe who aren't as technical or maybe aren't the
audience that you think they are to success quicker. And as I mentioned, content,
for sure, making it easier. Use cases is a big one and I'm not sure
whether you can figure out who that audience really is without
digging into those use cases. But then making sure that you
have content that speaks to those. And speaks to them in a way that
shares knowledge and not features, meaning that you understand the problem
that they have and that you are looking for ways to be able to help them solve
that and there's a website for that one too if you want to
read the full manifesto. Just a couple of other like non-content
ideas for giving people what they want. I think an API Explorer like what Dropbox
has here is a great way to be able to see some responses without
having to write some code. And then, of course, we're
all familiar with TwilioQuest. Also a talk tomorrow about
TwilioQuest, I believe so. And Patrick from Developer Mode who's
doing community projects in this vein is here as well. So, thinking about ways that you can
provide an experience that will be more welcoming to that audience
that you've now discovered. And recognizing, again, that
they live in this context of low code tools, and how can you incorporate
those into your portal or how can you make sure that the service that you have
is available on all of these tools. So, those are our three ways. Once you've rethought the audience to help
find out what they want and then help them to get it. And now we have a few seconds for you to
practice with your eyes again because this is what you're going to be doing as you
look at the data from your portal and you think about who is visiting it. Can you see, if you move from corner
to corner, your perspective change? And hopefully, you'll see
that in your audience as well. So, thank you. ♪ [music] ♪