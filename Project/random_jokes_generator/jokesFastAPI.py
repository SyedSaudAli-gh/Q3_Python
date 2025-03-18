from fastapi import FastAPI
import random

app = FastAPI()

pakistani_jokes = [
 {
        "id": 1,
        "setup": "Larka: Mujhse shadi karogi?",
        "punchline": "Larki: Tumhare paas bangla, gari, paisa hai? Larka: Nahi, par mere paas aik acha dil hai! Larki: Chalo, dil bech ke kuch le aao! 😂",
        "type": "Love Joke"
    },
    {
        "id": 2,
        "setup": "Ladka ladki ko propose karne laga...",
        "punchline": "Ladki boli: Tum cigarette peete ho? Ladka: Nahi! Ladki: Sharab? Ladka: Kabhi nahi! Ladki: Toh phir mere liye kya chhodo ge? 😆",
        "type": "Love Joke"
    },
    {
        "id": 3,
        "setup": "Biwi: Suno, tum mujhe ek aisi jagah le chalo jahan bohot sukoon ho!",
        "punchline": "Shohar: Chalo, tumhari ammi ke ghar chalte hain! 😂",
        "type": "Wife Joke"
    },
    {
        "id": 4,
        "setup": "Biwi ne kaha: Tum mujhse kitna pyar karte ho?",
        "punchline": "Shohar: Main tumhare bina jee nahi sakta! Biwi: Proof do! Shohar: Mujhe zindagi ka insurance karwane do! 🤣",
        "type": "Wife Joke"
    },
    {
        "id": 5,
        "setup": "Ladka apni crush se bola: Tum meri zindagi ho!",
        "punchline": "Crush: Ohhh, so sweet! Ladka: Haan, mujhe bhi ajeeb ajeeb sawal karti ho jaise meri maa! 😂",
        "type": "Love Joke"
    },
    {
        "id": 6,
        "setup": "Biwi: Aap mujhe kabhi koi gift kyun nahi dete?",
        "punchline": "Shohar: Tum mere liye gift ho! Biwi: Mujhe return policy chahiye! 🤣",
        "type": "Wife Joke"
    },
    {
        "id": 7,
        "setup": "Biwi ne gusse me kaha: Bas! Ab mai tumse baat nahi karungi!",
        "punchline": "Shohar: Shukar hai, finally ek masla to khud solve ho gaya! 😂",
        "type": "Wife Joke"
    },
    {
        "id": 8,
        "setup": "Larka apni mehbooba se: Mujhe tumse kuch zaroori baat karni hai...",
        "punchline": "Mehbooba: Mujhse shadi karni hai? Larka: Nahi yaar, tera Netflix ka password chahiye! 😆",
        "type": "Love Joke"
    },
    {
        "id": 9,
        "setup": "Biwi ne shohar se kaha: Suno, mujhe surprise chahiye!",
        "punchline": "Shohar: Achha, aankhein band karo! (Biwi ne aankhein band ki) Shohar: Ab kholo! Biwi: Kuch nazar nahi aa raha! Shohar: Surprise! Bijli ka bill nahi diya! 😂",
        "type": "Wife Joke"
    },
    {
        "id": 10,
        "setup": "Larka larki se: Tumhe kaise pata chalta hai ke main online hoon?",
        "punchline": "Larki: Kyunki tumhara ‘Last Seen’ mera ‘Home Page’ hai! 🤣",
        "type": "Love Joke"
    },
     {
        "id": 11,
        "setup": "Ek Pathan doctor ke paas gaya aur bola: Doctor sahab, jab bhi chai peeta hoon, ankhein dukhne lagti hain...",
        "punchline": "Doctor: Bhai, chammach to nikal diya karo cup se! 😂😂",
        "type": "Pathan Joke"
    },
    {
        "id": 12,
        "setup": "Biwi: Aap mujhe koi aisi jagah le chalo jahan bohot saare log na hoon, sirf hum dono hoon...",
        "punchline": "Shohar: Chal phir kitchen chalte hain! 🤣🤣",
        "type": "Marriage Joke"
    },  
    {
        "id": 13,
        "setup": "Teacher: Beta, koi aisa jumla banao jisme ‘shaam’ bhi aaye aur ‘mashwara’ bhi aaye...",
        "punchline": "Student: Ammi ne kaha, ‘Shaam tak ghar aajao, warna abba ka mashwara lag jayega!’ 🤣",
        "type": "School Joke"
    },
    {
        "id": 14,
        "setup": "Boy: Tum mujhse shadi karogi?",
        "punchline": "Girl: Tere paas BMW hai? Bungalow hai? Bank balance hai? 🤨 Boy: Nahi, par mere paas ek idea hai… Tujh se achi wali dhund leta hoon! 😂",
        "type": "Love Joke"
    },
    {
        "id": 15,
        "setup": "Pathan apni biwi ke saath restaurant gaya...",
        "punchline": "Waiter: Sir, aap kya lenge? Pathan: Bhai, hum dono ek hi plate me kha leinge! Biwi: Hayee, kitni mohabbat hai mujhse! Pathan: Nahi bhai, paisay kam hain! 😂😂",
        "type": "Restaurant Joke"
    },
    {
        "id": 16,
        "setup": "Doctor: Yeh chhoti chhoti beemariyan ho jati hain, koi bara masla nahi...",
        "punchline": "Patient: Masla bara tab hoga jab bill chhota nahi hoga! 🤣",
        "type": "Doctor-Patient Joke"
    },
    {
        "id": 17,
        "setup": "Ek aadmi railway track pe baitha tha...",
        "punchline": "Log bole: Bhai, train aa rahi hai, uth ja! Aadmi: Aray chill, idhar likha hai ‘Self Service’! 😂",
        "type": "Random Funny Joke"
    },
    {
        "id": 18,
        "setup": "Professor: Tumhari kitab kahan hai?",
        "punchline": "Student: Sir, airpod wale ka zamana hai, ab hum YouTube se parhte hain! 😂😂",
        "type": "Student Life Joke"
    },
    {
        "id": 19,
        "setup": "Biwi: Suno, mujhe ek chhota sa surprise chahiye...",
        "punchline": "Shohar: Theek hai, kal se tumhari pocket money band! 😆",
        "type": "Wife-Husband Joke"
    },
    {
        "id": 20,
        "setup": "Friend: Bhai, job mil gayi?",
        "punchline": "Berozgar: Haan yaar, subah uthanay wali alarm service start kar di hai, 10 rupey per call! 😂😂",
        "type": "Berozgar Life Joke"
    },
     {
        "id": 21,
        "setup": "Teacher: Beta, agar tumne dobara class me shor machaya to ghar chalay jaana!",
        "punchline": "Student: Sir, paisay to dena, ghar jane ke liye rikshaw lena hai! 🤣",
        "type": "Badtameez Student Joke"
    },
    {
        "id": 22,
        "setup": "Teacher: Beta, is jumlay ka angrezi me tarjuma karo: ‘Main school ja raha hoon’!",
        "punchline": "Student: ‘I am going to hell!’ Teacher: Kya?? Student: Sorry sir, galti se sach nikal gaya! 😂",
        "type": "Savage Student Joke"
    },
    {
        "id": 23,
        "setup": "Teacher: Jab Einstein peda hua to duniya me kya tabdili aayi?",
        "punchline": "Student: Sir, ek aur bechara school ka shikar ho gaya! 🤣",
        "type": "Funny School Joke"
    },
    {
        "id": 24,
        "setup": "Teacher: Beta, tum class me so kyun rahe ho?",
        "punchline": "Student: Sir, aap ki baatein sunte sunte aankhein band ho jati hain, bilkul jaise YouTube ki ads skip ho jati hain! 😂",
        "type": "Savage Student Joke"
    },
    {
        "id": 25,
        "setup": "Teacher: Tum exam me fail kyun hue?",
        "punchline": "Student: Sir, aap hi to kehte hain, ‘Galti se seekho’… to maine jaan bujh ke galtiyan ki! 😆",
        "type": "Badtameez Student Joke"
    },
    {
        "id": 26,
        "setup": "Teacher: Tum itne buddhu kyun ho?",
        "punchline": "Student: Sir, ye to genetic problem hai, aap ke lectures ka koi lena dena nahi! 😂",
        "type": "Badtameez Student Joke"
    },
    {
        "id": 27,
        "setup": "Teacher: Beta, yeh batao ki ‘Homework’ ka maqsad kya hota hai?",
        "punchline": "Student: Sir, ‘Student ka dimag kharab karna aur uski maa ka test lena’! 🤣",
        "type": "Funny Homework Joke"
    },
    {
        "id": 28,
        "setup": "Teacher: Tumne test me likha ‘I don’t know’? Ye kya hai?",
        "punchline": "Student: Sir, sach bolna acha hota hai na! 😂",
        "type": "Funny Test Joke"
    },
    {
        "id": 29,
        "setup": "Teacher: Agar tum class me shor machaoge to principal ke paas bhej dunga!",
        "punchline": "Student: Sir, wo bhi koi dhamki hai? Wahan WiFi fast chalta hai! 😆",
        "type": "Badtameez Student Joke"
    },
    {
        "id": 30,
        "setup": "Teacher: Beta, tum maths me itne weak kyun ho?",
        "punchline": "Student: Sir, kyunki mujhe lagta hai, aap ki umar ho gayi hai, aap hi ginti bhool gaye ho! 🤣",
        "type": "Savage Student Joke"
    },
     {
        "id": 31,
        "setup": "Teacher: Beta, tum itne din se school kyun nahi aaye?",
        "punchline": "Student: Sir, ghar wale kehte hain school wale insan bana dete hain, par mujhe janwar pasand hain! 😆",
        "type": "Badmash Student Joke"
    },
    {
        "id": 32,
        "setup": "Teacher: Beta, tumhari likhai itni gandi kyun hai?",
        "punchline": "Student: Sir, aap doctor ki nayi nayi degree dekh rahe hain! 😂",
        "type": "Handwriting Joke"
    },
    {
        "id": 33,
        "setup": "Teacher: Tum class me itna shor kyun machate ho?",
        "punchline": "Student: Sir, kyunki aap boring lecture dete hain, aur mujhe life me thrill chahiye! 🤣",
        "type": "Savage Student Joke"
    },
    {
        "id": 34,
        "setup": "Teacher: Tumne homework kyun nahi kiya?",
        "punchline": "Student: Sir, jo cheez humare future me kaam nahi aani, uspe time waste nahi karte! 😂",
        "type": "Homework Joke"
    },
    {
        "id": 35,
        "setup": "Teacher: Beta, agar main tumhara paper check karun to mujhe kya milega?",
        "punchline": "Student: Sir, sirf depression milega! 😆",
        "type": "Exam Joke"
    },
    {
        "id": 36,
        "setup": "Teacher: Beta, tum fail kyun ho gaye?",
        "punchline": "Student: Sir, question paper mere syllabus se bahar tha, aur answers mere dimaag se! 🤣",
        "type": "Fail Student Joke"
    },
    {
        "id": 37,
        "setup": "Teacher: Tum class me itne zyada kyun haste ho?",
        "punchline": "Student: Sir, aapka chehra dekh kar mujhe meri kismat yaad aa jati hai! 😂",
        "type": "Funny Teacher Joke"
    },
    {
        "id": 38,
        "setup": "Teacher: Tum exam me fail ho gaye, sharam nahi aayi?",
        "punchline": "Student: Sir, sharam to aapko aani chahiye, aapke parhaye huye se to pass hona hi mushkil hai! 😆",
        "type": "Savage Student Joke"
    },
    {
        "id": 39,
        "setup": "Teacher: Beta, subject ka naam batao jo tumhe pasand hai.",
        "punchline": "Student: Lunch break! 😆",
        "type": "Funny Student Joke"
    },
    {
        "id": 40,
        "setup": "Teacher: Tum itni baatein kyun karte ho?",
        "punchline": "Student: Sir, baatein karna ek art hai, aur main artist hoon! 😂",
        "type": "Savage Student Joke"
    }
]

@app.get("/pakistani_joke")
def get_pakistani_joke():
    """Returns a random Pakistani joke"""
    random_pakistani_joke = random.choice(pakistani_jokes)
    return random_pakistani_joke
