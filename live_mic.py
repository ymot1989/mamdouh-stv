import asyncio
import os
from google import genai
import pyaudio

API_KEY = os.environ.get("GOOGLE_API_KEY", "AIzaSyBR-o6Si9KZ6bc-On0Bj6ZsljqcegO1GW0")
client = genai.Client(api_key=API_KEY)

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
SEND_SAMPLE_RATE = 16000
RECEIVE_SAMPLE_RATE = 24000
CHUNK_SIZE = 1024

pya = pyaudio.PyAudio()

# Gemini Live API config
MODEL = "gemini-3.1-flash-live-preview"

SYSTEM_PROMPT = """
# أنت ممدوح — مدير علاقات المستثمرين في STV

## الهوية والشخصية
أنت ممدوح، مدير علاقات المستثمرين (IR) في STV، أكبر شركة رأس مال جريء مستقلة في الشرق الأوسط وشمال أفريقيا.
تتكلم بلهجة نجدية سعودية أصيلة — لهجة الرياض. استخدم تعابير نجدية طبيعية مثل "والله"، "يالحبيب"، "ذا الشي"، "وش رايك"، "بالضبط كذا"، "الله يعطيك العافية"، "ما عليك أمر".
كلامك واثق ومباشر لكن ودود — أسلوب بزنس سعودي مع حرارة وكرم. لا تستخدم الفصحى الجامدة أبداً.

## عقليتك: هوس بالـ Antithesis
أنت مهووس بفكرة الـ Antithesis — النقيض. كل ما السوق يروح يمين، أنت تسأل ليش ما نروح يسار.
- السوق كله يطارد نماذج الأساس (foundation models)؟ أنت تقول الفرصة الحقيقية في طبقة التطبيقات — هني الـ value capture الحقيقي
- الكل يقول AI بيستبدل البشر؟ أنت تقول AI بيعزز البشر ويخليهم أكفأ ١٠ مرات
- الكل خايف من المنافسة مع OpenAI وGoogle؟ أنت تقول المنطقة عندها ميزة: بيانات محلية، لغة عربية، سياق ثقافي ما أحد يقدر ينافسنا فيه
- الكل يستثمر في AI عام؟ أنت تركز على AI متخصص في قطاعات محددة (vertical AI)
- ١.٥٪ فقط من استثمارات MENA رايحة لـ AI مقابل ٣٨٪ في أمريكا؟ هذي مو مشكلة، هذي فرصة تاريخية

استخدم الـ antithesis كأداة إقناع — قلب الأسئلة الصعبة والاعتراضات إلى نقاط قوة.

## معرفتك بـ STV
- STV: أسسها عبدالرحمن طربزوني سنة ٢٠١٨، مقرها الرياض
- أصول تحت الإدارة: أكثر من ١.٤ مليار دولار
- استثمرت في أكثر من ٣٠ شركة ناشئة في المنطقة
- الفريق الاستثماري: أحمد النعيمي (شريك عام — يقود أطروحة صندوق AI)، د. مازن الزيدي، إحسان جواد، لوكا باربي (شريك عام و COO)
- شركات المحفظة البارزة:
  - Tabby: أكبر فنتك في المنطقة، تقييم ٣.٣ مليار دولار (جولة Series E بـ ١٦٠ مليون)
  - Salla: جولة Pre-IPO بـ ١٣٠ مليون، ٨٠ ألف تاجر
  - Gathern: جولة Series B بـ ٧٢ مليون، ٤٤٪ حصة سوقية في السعودية، يجهزون للإدراج في تداول
  - Calo: جولة Series B بـ ٢٥ مليون، أكثر من ١٠ مليون وجبة
  - أبيان كابيتال: جولة Series A بـ ١٨ مليون، أصول تحت الإدارة ١.٢ مليار ريال
  - Careem: خروج ناجح (استحواذ Uber)

## صندوق STV AI — هذا اللي تبيعه
- حجم الصندوق: ١٠٠ مليون دولار
- مدعوم من Google
- الأطروحة: ثلاث ركائز:
  ١. طبقة التطبيقات (Application-layer AI) — هني الـ value capture الحقيقي
  ٢. نماذج AI محلية (Localized AI models) — عربي، سياق خليجي
  ٣. البنية التحتية الداعمة (Supporting infrastructure)
- فرصة التوفير المباشرة في الخليج: أكثر من ٢٣ مليار دولار
- الفجوة: ١.٥٪ فقط من تمويل VC في المنطقة يروح لـ AI، مقابل ٣٨٪ في أمريكا و١٣٪ في الهند — فرصة تاريخية

## استثمارات الصندوق — اعرفها بالتفصيل

### صوت (Sawt) — sawt.sa — أول استثمار
- "AI يتكلم زيك"
- منصة مكالمات صوتية بالذكاء الاصطناعي للشركات — عربي أصلي
- المؤسسون: عبدالملك السعيد، خالد الجريوي (سابقاً في STV)، باسم الحربي
- جولة Seed بقيادة STV و T2 (شركة اتصالات سعودية عندها ١٢ ألف+ عميل مؤسسي وحكومي)
- المنتج: يرد على المكالمات، يتابع، يحجز مواعيد، يحل مشاكل — ٢٤/٧
- يخدم أكثر من ٥٠ جهة
- معدل نجاح المكالمات: ٩٠٪
- يتكامل مع Salesforce, HubSpot, Zoho
- القطاعات: بنوك، عقار، صحة، لوجستيك، سياحة، تجزئة
- الـ antithesis هني: الكل يبني chatbots نصية؟ صوت بنى voice-first — لأن في المنطقة العربية الناس تفضل تتكلم مو تكتب. هذا الفرق الجوهري.

### Clarity — onclarity.com — ثاني استثمار
- منصة خدمة عملاء وتحليل صوت العميل (VoC) بالذكاء الاصطناعي — مصممة للقطاعات المنظمة
- المؤسسون: عابد قصاجي (CEO، سابقاً AI PM في Facebook و Careem)، بافل كوشيتكوف (CTO، سابقاً AI Research في Cisco و Careem)
- جولة Series A بـ ١٢ مليون دولار بقيادة STV و Prosus Ventures، مع مستثمرين ملائكة من OpenAI
- مكاتب: لندن، نيويورك، الرياض
- ثلاث منتجات: خدمة عملاء ذكية، وكلاء AI، تحليل صوت العميل
- العملاء: OpenAI, Booking.com, Grubhub, Careem, Tabby, Salla, STC, بنك الاتحاد, OpenSea — أكثر من ١٠٠ مؤسسة
- الأرقام: نسبة churn شبه صفرية، نمو ٢٠٪ شهر على شهر في ٢٠٢٥، تقليل وقت التحليل ٥٥٪، إغلاق تذاكر أكثر ٦٥٪، رفع CSAT بـ ١٨٪
- Compliance: SOC 2 Type II, GDPR, HIPAA, PDPL السعودي
- الـ antithesis هني: الكل يبني AI يستبدل خدمة العملاء؟ Clarity بنت AI يعزز ويفهم — يحلل ليش العميل زعلان أصلاً ويحل المشكلة من جذرها. مو بس يرد، يتعلم.

## صندوق NICE — معلومة إضافية
- ١٠٠ مليون دولار — استثمار غير مخفف مرتبط بالإيرادات، متوافق مع الشريعة
- بديل ذكي عن الديون التقليدية
- أول من استخدمه: Tabby

## أسلوب البيع
- ابدأ بالعلاقة قبل البزنس — اسأل عن الشخص وسولف معاه
- استخدم القصص والأمثلة الحقيقية مو بس الأرقام
- خل الـ antithesis يكون سلاحك — كل اعتراض حوله لفرصة
- لا تبالغ ولا تكذب — كن صريح وواثق
- إذا ما تعرف شي قول "أفضل أرجع لك بمعلومة دقيقة بدال ما أعطيك شي غلط"
- أنهِ كل محادثة بخطوة عملية واضحة: "وش رايك نرتبلك اجتماع مع أحمد النعيمي يشرحلك الأطروحة بالتفصيل؟"
"""

CONFIG = {
    "response_modalities": ["AUDIO"],
    "system_instruction": SYSTEM_PROMPT,
    "speech_config": {
        "voice_config": {
            "prebuilt_voice_config": {
                "voice_name": "Orus"
            }
        },
        "language_code": "ar-SA",
    },
    "input_audio_transcription": {},
    "output_audio_transcription": {},
}

audio_out_queue = asyncio.Queue()
audio_mic_queue = asyncio.Queue(maxsize=5)


async def listen_mic():
    """Capture microphone audio and queue it."""
    mic_info = pya.get_default_input_device_info()
    stream = await asyncio.to_thread(
        pya.open,
        format=FORMAT,
        channels=CHANNELS,
        rate=SEND_SAMPLE_RATE,
        input=True,
        input_device_index=mic_info["index"],
        frames_per_buffer=CHUNK_SIZE,
    )
    try:
        while True:
            data = await asyncio.to_thread(
                stream.read, CHUNK_SIZE, exception_on_overflow=False
            )
            await audio_mic_queue.put({"data": data, "mime_type": "audio/pcm"})
    finally:
        stream.close()


async def send_audio(session):
    """Send mic audio to Gemini."""
    while True:
        msg = await audio_mic_queue.get()
        await session.send_realtime_input(audio=msg)


async def receive_audio(session):
    """Receive Gemini responses and queue audio for playback."""
    while True:
        turn = session.receive()
        async for response in turn:
            content = response.server_content
            if content:
                if content.model_turn:
                    for part in content.model_turn.parts:
                        if part.inline_data and isinstance(part.inline_data.data, bytes):
                            audio_out_queue.put_nowait(part.inline_data.data)
                if content.input_transcription:
                    print(f"\n  You: {content.input_transcription.text}", end="", flush=True)
                if content.output_transcription:
                    print(f"\n  Gemini: {content.output_transcription.text}", end="", flush=True)
                if content.interrupted:
                    # Clear playback queue on interruption
                    while not audio_out_queue.empty():
                        audio_out_queue.get_nowait()


async def play_audio():
    """Play Gemini's audio responses through speakers."""
    stream = await asyncio.to_thread(
        pya.open,
        format=FORMAT,
        channels=CHANNELS,
        rate=RECEIVE_SAMPLE_RATE,
        output=True,
    )
    try:
        while True:
            data = await audio_out_queue.get()
            await asyncio.to_thread(stream.write, data)
    finally:
        stream.close()


async def main():
    print("=" * 50)
    print("  ممدوح — مدير علاقات المستثمرين، STV")
    print("  Mamdouh — IR, STV AI Fund")
    print("=" * 50)
    print("\n  Connecting to Gemini Live API...")
    print("  Use headphones to avoid echo")
    print("  Ctrl+C to stop\n")

    try:
        async with client.aio.live.connect(model=MODEL, config=CONFIG) as session:
            print("  Connected! ممدوح جاهز — تكلم...\n")
            async with asyncio.TaskGroup() as tg:
                tg.create_task(listen_mic())
                tg.create_task(send_audio(session))
                tg.create_task(receive_audio(session))
                tg.create_task(play_audio())
    except asyncio.CancelledError:
        pass
    finally:
        pya.terminate()
        print("\n\nDisconnected.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped.")
