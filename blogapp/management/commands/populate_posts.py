from blogapp.models import post,Category
from django.core.management.base import BaseCommand
import random



class Command(BaseCommand):
    help='This is command insert the post data'

    def handle(self, *args, **kwargs):

        #deleting existing data from DB
        post.objects.all().delete()

        post_ids = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]
        #     "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        #     "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        #     "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
        #     "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4",
        #     "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4"
        # ]

        titles = [
            "The Power of Morning Routines",
            "Why Traveling Solo is Life-Changing",
            "The Joy of Reading Fiction",
            "Simple Ways to Practice Gratitude",
            "How Music Heals the Soul",
            "The Magic of Evening Walks",
            "How Cooking Boosts Creativity",
            "The Calmness of Meditation",
            "Why Journaling Clears the Mind",
            "Lessons Learned from Failure",
            "Finding Peace in Nature",
            "The Strength of Lifelong Learning",
            "Digital Detox: Why It Matters",
            "Acts of Kindness That Change Lives",
            "The Beauty of Minimalism"
        ]

        authors = [
            "Sophia Sharma",
            "Arjun Mehta",
            "Emily Verma",
            "Rahul Iyer",
            "Nisha Kapoor",
            "Karan Bhatia",
            "Meera Rao",
            "Ananya Deshmukh",
            "Vikram Singh",
            "Priya Menon",
            "Rohan Gupta",
            "Tanvi Joshi",
            "Aditya Kulkarni",
            "Sneha Pillai",
            "Devansh Khurana"
        ]

        contents = [
            """Starting your day with a well-planned morning routine can set the tone for success. 
            Simple habits like meditation, exercise, journaling, or even drinking water can increase productivity, 
            reduce stress, and improve your focus throughout the day.""",

            """Traveling alone might sound intimidating, but it allows you to explore new cultures at your own pace. 
            You gain confidence, independence, and a deeper connection with yourself. 
            Every trip becomes a story of self-discovery and courage.""",

            """Fiction books are more than stories—they transport us into new worlds, 
            expand imagination, and help us understand emotions deeply. 
            Reading for just 30 minutes a day can reduce stress and boost creativity.""",

            """Gratitude is a small habit with a big impact. 
            By writing down three things you're thankful for every day, you shift your mindset toward positivity. 
            It helps you build stronger relationships and live a happier life.""",

            """Music isn’t just entertainment—it’s therapy. 
            Listening to calming music can lower blood pressure, improve sleep, and release dopamine. 
            From classical to lo-fi beats, every tune has the power to heal.""",

            """Taking a walk in the evening helps clear your mind after a busy day. 
            It improves digestion, reduces anxiety, and gives you space to reflect in peace.""",

            """Cooking isn’t just about food—it’s about creativity. 
            Experimenting with flavors and recipes sparks imagination and builds patience.""",

            """Meditation offers a way to quiet the noise within. 
            Even 10 minutes of mindful breathing can reduce stress and increase self-awareness.""",

            """Journaling clears the mental clutter. 
            Writing down your thoughts helps you process emotions and discover hidden insights.""",

            """Failure is not the end—it’s a lesson in disguise. 
            Each setback brings resilience, wisdom, and a stronger sense of direction.""",

            """Spending time in nature reconnects us with simplicity. 
            Fresh air, greenery, and silence restore balance and inspire gratitude.""",

            """Lifelong learning keeps the mind sharp. 
            Exploring new skills or subjects builds confidence and keeps curiosity alive.""",

            """Constant notifications drain focus. 
            A digital detox restores attention, improves sleep, and brings back real human connection.""",

            """A small act of kindness—like a smile, a note, or a helping hand—can ripple through someone’s life 
            in ways you may never know.""",

            """Minimalism is more than decluttering—it's about living with intention. 
            Owning less creates space for peace, focus, and joy in the essentials."""
        ]

        img_urls = [
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
            "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
            "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4",
            "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4",
            "https://images.unsplash.com/photo-1503264116251-35a269479413",
            "https://images.unsplash.com/photo-1512058564366-c9e8b12a0e2b",
            "https://images.unsplash.com/photo-1523978591478-c753949ff840",
            "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
            "https://images.unsplash.com/photo-1522202757853-68adf38b47e6",
            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
            "https://images.unsplash.com/photo-1531266754282-63a41184d1d0",
            "https://images.unsplash.com/photo-1521747116042-5a810fda9664",
            "https://images.unsplash.com/photo-1503676260728-1c00da094a0b",
            "https://images.unsplash.com/photo-1507089947368-19c1da9775ae"
        ]



        categories=Category.objects.all()

        for post_id,title,Author,content,img_url in zip(post_ids,titles,authors,contents,img_urls):

            catagory = random.choice(categories)

            post.objects.create(title=title,Author=Author,content=content,img_url=img_url,post_id=post_id,category=catagory)

        self.stdout.write(self.style.SUCCESS("Insertion Completed..."))