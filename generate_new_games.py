import subprocess
import os
import time
import glob
import sys

BASE_DIR = '/Users/sym/code/elden_ring_liveaction'

TASKS = [
    # ── Cyberpunk 2077 ──
    {
        'id': 'cp01_judy',
        'game': 'cyberpunk',
        'name': '朱迪·阿尔瓦雷斯 (Judy Alvarez)',
        'target_dir': os.path.join(BASE_DIR, 'cyberpunk'),
        'target_file': '01_judy_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机室内微光实拍的真实女性肖像：扮演《赛博朋克2077》朱迪·阿尔瓦雷斯（Judy Alvarez）的真实拉美裔年轻女性特写。纯相机实拍风格，极度写实的真人活人感，像用索尼A7R5搭配85mm f/1.4镜头拍摄的真实人像。一位20多岁性格不羁的真实年轻女孩，面部呈现完全未修图的自然小麦色皮肤，肉眼可见的细微毛孔、微小面部痣点与自然的唇纹，右耳侧颈部有着做旧机械义体神经接口的真实金属与皮肤接缝。五彩染发的湿润发丝自然垂落在额前，颈部与手臂上有逼真的褪色手绘纹身纹理。她身穿磨损做旧的莫克斯帮工装背带牛仔裤与紧身背心，正斜靠在夜之城地下超梦工作室的破旧皮椅上，周围散落着真实杂乱的线缆与微弱闪烁的霓虹冷光灯管。真实的室内弱光浅景深摄影，没有CG、3D模型或数字绘画感，完全是一张真实生活中的人物实拍照片。'
    },
    {
        'id': 'cp02_johnny',
        'game': 'cyberpunk',
        'name': '强尼·银手 (Johnny Silverhand)',
        'target_dir': os.path.join(BASE_DIR, 'cyberpunk'),
        'target_file': '02_johnny_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机抓拍的真实摇滚老炮硬汉照片：扮演《赛博朋克2077》强尼·银手（Johnny Silverhand）的真实中老年男士肖像。纯相机实拍风格，极度震撼的活人感，像用佳能EOS单反在后台抓拍的摇滚乐手纪实。一位50岁左右消瘦而充满棱角的硬汉，留着油腻凌乱的黑发与花白下颌胡茬，面容沧桑，眼角布满真实的皱纹与晒斑，疲惫深邃的双眼透过复古飞行员墨镜边缘凝视镜头。他左臂是一条由真实工业级不锈钢与冷锻机械铰链打造的银色义肢假肢道具，金属表面有真实的工业划痕、润滑油渍与螺栓细节。身穿满是磨损折痕的黑色真皮马甲，脖颈挂着狗牌项链。背景是烟雾弥漫的夜之城地下摇滚酒吧后台，红蓝霓虹灯在汗湿皮肤与金属手臂上形成真实的光学反射。绝无3D平滑CG与磨皮假人感，纯正纪实摄影。'
    },
    {
        'id': 'cp03_panam',
        'game': 'cyberpunk',
        'name': '帕南·帕尔默 (Panam Palmer)',
        'target_dir': os.path.join(BASE_DIR, 'cyberpunk'),
        'target_file': '03_panam_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在恶土夕阳下抓拍的真实女性照片：扮演《赛博朋克2077》阿德卡多流浪者帕南·帕尔默（Panam Palmer）的真实年轻女性肖像。纯相机实拍风格，极度写实的活人感，像国家地理摄影师在沙漠中抓拍的人物特写。一位20多岁健康小麦肤色的非裔/混血女性，面容坚毅英气，面颊上带有真实的微小汗珠、细微沙尘颗粒与自然雀斑，唇部有天然的唇纹，深棕色长发随狂风凌乱飞舞。她身穿做旧缝补的红白双色流浪者厚帆布夹克与磨损牛仔裤，单手斜靠在沾满厚厚泥土沙尘的越野改装皮卡车门边。背景是黄昏夕阳下辽阔荒凉的恶土沙漠与远处耸立的输电铁塔，金色余晖硬光勾勒出面部轮廓与车身粗糙漆面。真实的户外自然光抓拍，完全剔除CG模型与二次元感，极其生动逼真的活人纪实照。'
    },
    {
        'id': 'cp04_nightcity_v',
        'game': 'cyberpunk',
        'name': '夜之城雨夜街头与雇佣兵 V (Night City Rainy Street / V)',
        'target_dir': os.path.join(BASE_DIR, 'cyberpunk'),
        'target_file': '04_nightcity_v_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机夜景高速快门实拍的真实街头抓拍照片：一位真实的年轻雇佣兵漫步在《赛博朋克2077》夜之城歌舞伎町雨夜街头。纯相机实拍风格，极度写实的现场感。前景是一位穿着做旧磨损的武士高领立领飞行员夹克的真实年轻混血青年侧身背影，领口微弱的黄光照亮湿透的发尾与颈部皮肤，面容在侧逆光中呈现未修图的真实毛孔与细微雨珠。他正站在布满水洼与垃圾的狭窄潮湿小巷中，地面雨水倒映着两旁密密麻麻的中文与日文粉红、翠绿霓虹灯招牌。身旁拉面摊位上冒出真实的腾腾白色蒸汽，细微雨丝在夜色车灯与霓虹光晕中划过一道道光痕。真实的光学夜景大光圈摄影，焦外散景自然柔和，镜头表面带有轻微水汽光晕，绝非游戏引擎渲染或3D概念画，充满赛博朋克现实温度的真实快门抓拍。'
    },

    # ── The Legend of Zelda: Breath of the Wild ──
    {
        'id': 'zelda01_princess',
        'game': 'zelda',
        'name': '塞尔达公主 (Princess Zelda)',
        'target_dir': os.path.join(BASE_DIR, 'zelda'),
        'target_file': '01_zelda_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在海拉鲁原野实拍的真实女性学者肖像：扮演《塞尔达传说：旷野之息》塞尔达公主（Princess Zelda）的真实年轻欧洲女性特写。纯相机实拍风格，极度写实的真人活人感，像用佳能EOS R5搭配85mm f/1.4镜头拍摄的真实人像。一位18-20岁的真实金发年轻女孩，面容端庄温婉却带着学术求索的专注与淡淡哀伤，完全未精修的自然白皙皮肤，肉眼可见的细密毛孔、微小雀斑与自然的唇纹，脸颊上带有草地勘探留下的微小泥灰痕迹。浅金色长发扎着发辫，有几缕凌乱碎发在微风中拂过耳畔。她身穿实物手工缝制的英杰深蓝色亚麻长袍与深色皮质调查短裤，怀中双手捧着一块由风化石板与黄铜镶边制成的“希卡之石”实物道具，表面泛着微弱幽蓝光芒。背景是开满野花的明媚海拉鲁青翠草原与古老长满青苔的石柱遗迹，柔和自然天光，浅景深虚化，绝无动漫塑料感、无3D建模CG感，完全是一张真实生活中的人物实拍照片。'
    },
    {
        'id': 'zelda02_link',
        'game': 'zelda',
        'name': '英杰林克 (Link, the Champion)',
        'target_dir': os.path.join(BASE_DIR, 'zelda'),
        'target_file': '02_link_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在户外实拍的真实青年剑士抓拍照片：扮演《塞尔达传说：旷野之息》林克（Link）的真实年轻战士特写。纯相机实拍风格，极度写实的活人感，像用索尼A7R5单反抓拍的真实动作演员肖像。一位身材敏捷精悍的20岁左右青年，浅棕金色的散乱短发被风吹得贴在额前，一双清澈、专注而饱经战事的深蓝眼眸流露出坚毅与警惕的活人眼神，下颌带有一道细微的浅浅疤痕，皮肤呈现风吹日晒的自然微红光泽与清晰毛孔。他身穿由粗纺天蓝色亚麻布手工缝制的英杰服，胸前交叉着深棕色皮革剑带，单手握着一柄带有岁月风蚀暗痕与微小缺口的钢质大师之剑剑柄。背景是初晨薄雾笼罩的科摩罗湖边红树林与泥泞岸边，清晨湿润微凉的环境自然光，镜头质感极度纯正，绝对没有任何动漫二次元、CG动画或油画涂抹感，极具生命力的少年剑士实拍。'
    },
    {
        'id': 'zelda03_urbosa',
        'game': 'zelda',
        'name': '格鲁德英杰 乌尔波扎 (Urbosa, Gerudo Champion)',
        'target_dir': os.path.join(BASE_DIR, 'zelda'),
        'target_file': '03_urbosa_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在沙漠强光下实拍的真实女性勇士照片：扮演《塞尔达传说：旷野之息》格鲁德英杰乌尔波扎（Urbosa）的真实中东/北非裔高大女性战士肖像。纯相机实拍风格，震撼写实的真人活人感。一位身材高挑强健、五官深邃英朗的30多岁女战神，面部呈现健康紧致的深古铜色皮肤，肉眼可见的真实毛孔与细腻汗光，眼角画着格鲁德风格古朴眼线，嘴角带着霸气从容的微笑。一头鲜艳浓密的深红色编织长发垂在肩后，身穿由纯铜手工雕花板甲与青金石宝石镶嵌的战甲，搭配飘逸的翠绿色英杰饰带。她单手握着一柄做旧圆月弯刀，另一手提着做旧金属圆盾。背景是骄阳炙烤下泛着热浪金光的格鲁德广袤沙丘，强烈真实的日光与阴影对比，彻底剔除3D假人和磨皮二次元感，极具力量美感的真实女勇士肖像摄影。'
    },
    {
        'id': 'zelda04_hyrule_vista',
        'game': 'zelda',
        'name': '海拉鲁城堡废墟远眺与流浪旅人 (Hyrule Castle & Great Plateau Vista)',
        'target_dir': os.path.join(BASE_DIR, 'zelda'),
        'target_file': '04_hyrule_vista_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机广角镜头实拍的真实人物探险抓拍照片：一位身穿旅行斗篷的真实探险者站在《塞尔达传说：旷野之息》初始台地悬崖边缘远眺海拉鲁城堡。纯相机实拍风格，极度写实的现场感与活人呼吸感。画面前景是一位身穿粗厚磨损风化绿亚麻斗篷与皮甲背包的真实年轻旅行者背影与侧脸，被高空山风刮得凌乱的真实发丝与衣角翻飞，双手扶在长满地衣青苔的断裂古代石栏上。中景是连绵起伏、郁郁葱葱的广袤原始松树森林与散落的古代守护者残骸；远景是清晨金光薄雾之中、被丝丝紫红色灾厄烟雾缭绕的宏伟哥特式海拉鲁城堡废墟。清晨湿润微凉的自然空气透视与柔和逆光光晕，高速快门捕捉到风中的微尘颗粒，绝非游戏CG截图、无3D假模型感，一张震撼人心的国家地理级大自然与遗迹远足摄影照片。'
    }
]

def generate_one(task):
    target_path = os.path.join(task['target_dir'], task['target_file'])
    if os.path.exists(target_path) and os.path.getsize(target_path) > 100000:
        print(f"[{task['id']}] Already exists ({os.path.getsize(target_path)/1024:.1f} KB), skipping.", flush=True)
        return True

    print(f"\n==========================================", flush=True)
    print(f"Starting [{task['id']}] - {task['name']} ({task['game']})", flush=True)
    print(f"==========================================", flush=True)

    before_files = set(glob.glob(os.path.join(task['target_dir'], '*.png')))

    cmd = [
        'opencli', 'chatgpt', 'image',
        task['prompt'],
        '--op', task['target_dir'],
        '--timeout', '240'
    ]

    start_time = time.time()
    res = subprocess.run(cmd, capture_output=True, text=True)
    elapsed = time.time() - start_time
    print(f"Process completed in {elapsed:.1f}s, exit code: {res.returncode}", flush=True)
    if res.stdout:
        print("Stdout:\n" + res.stdout.strip(), flush=True)
    if res.stderr:
        print("Stderr:\n" + res.stderr.strip(), flush=True)

    after_files = set(glob.glob(os.path.join(task['target_dir'], '*.png')))
    new_files = list(after_files - before_files)

    if new_files:
        newest = sorted(new_files, key=lambda f: os.path.getmtime(f), reverse=True)[0]
        os.rename(newest, target_path)
        print(f"SUCCESS: Saved as {task['target_file']} ({os.path.getsize(target_path)/1024:.1f} KB)", flush=True)
        return True
    else:
        chatgpt_files = sorted(glob.glob(os.path.join(task['target_dir'], 'chatgpt_*.png')), key=lambda f: os.path.getmtime(f), reverse=True)
        if chatgpt_files:
            latest = chatgpt_files[0]
            os.rename(latest, target_path)
            print(f"SUCCESS (from latest chatgpt_*): Saved as {task['target_file']} ({os.path.getsize(target_path)/1024:.1f} KB)", flush=True)
            return True
        print(f"ERROR: No new image detected for {task['id']}", flush=True)
        return False

def main():
    success_count = 0
    total = len(TASKS)
    for i, task in enumerate(TASKS):
        print(f"\n>>> Progress: [{i+1}/{total}] Processing {task['name']}...", flush=True)
        for attempt in range(2):
            if generate_one(task):
                success_count += 1
                time.sleep(4)
                break
            else:
                print(f"Retrying {task['id']} (attempt {attempt+2})...", flush=True)
                time.sleep(6)

    print(f"\n==========================================", flush=True)
    print(f"All new tasks finished! {success_count}/{total} images generated successfully.", flush=True)
    print(f"==========================================", flush=True)

if __name__ == '__main__':
    main()
