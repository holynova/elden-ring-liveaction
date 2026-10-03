import subprocess
import os
import time
import glob

OUTPUT_DIR = '/Users/sym/code/elden_ring_liveaction/generated'
os.makedirs(OUTPUT_DIR, exist_ok=True)

TASKS = [
    {
        'id': '01_leyndell',
        'name': '王城罗德尔 (Leyndell, Royal Capital)',
        'target_file': '01_leyndell_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的王城罗德尔（Leyndell, Royal Capital）。宏伟壮丽的古罗马与拜占庭风格黄金巨城，由厚重的砂岩与精雕细琢的金色圆顶宫殿群组成。天空中矗立着无比巨大的、散发着神圣温暖金光的黄金树，半透明的黄金叶片在薄雾中飘落。前景是高耸的城墙回廊与巨型石雕，城中升起袅袅晨雾。真实的建筑风化质感、宏大史诗感，35mm电影胶片实拍质感，暗黑奇幻史诗电影剧照。'
    },
    {
        'id': '02_tree_sentinel',
        'name': '大树守卫 (Tree Sentinel)',
        'target_file': '02_tree_sentinel_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的大树守卫（Tree Sentinel）。一位身穿沉重华丽金铜浮雕板甲的中世纪巨骑士，身形威猛，骑在一匹披挂着重型金色马铠的巨大战马背上。他单手紧握沉重的黄金戟，另一手持厚重的圣树黄金大盾。阳光透过秋季林间的金色落叶洒在他斑驳风化的金属盔甲上。战马踏在泥泞的青苔古道上，呼吸喷出白雾。极度写实的金属光泽、泥土污痕与马匹毛发细节，高预算史诗电影质感剧照。'
    },
    {
        'id': '03_volcano_manor',
        'name': '火山官邸 (Volcano Manor)',
        'target_file': '03_volcano_manor_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的火山官邸（Volcano Manor）。格密尔火山之巅一座阴森奢华的哥特维多利亚风古老贵族庄园大厅。窗外是黑石嶙峋的火山岩浆赤红色暗光与翻滚的火山灰烟尘，大厅内铺着深红色天鹅绒长毯，悬挂着点燃昏黄烛火的繁复黑铁吊灯。庄园女主人塔妮丝身着华贵苍白丝绸长裙与神秘面具静坐在高背天鹅绒座椅上，身旁站着手持重剑的沉重铁甲叛律骑士。沉郁、堕落、典雅的暗黑奇幻电影剧照。'
    },
    {
        'id': '04_malenia',
        'name': '女武神 玛莲妮亚 (Malenia, Blade of Miquella)',
        'target_file': '04_malenia_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人肖像剧照：艾尔登法环中的女武神玛莲妮亚（Malenia, Blade of Miquella）。真人实景风格，一位身材挺拔修长的红发女武士，橘红色长发在微风中飘散。她右臂装配着精美绝伦的风化纯金义手假肢，头戴带飞翼的金质头盔，身披破损的红色战袍。站在圣树根系环绕的幽深水池中，手中紧握一柄修长锋利的无护手金色太刀。皮肤真实自然带有轻微战痕，金黄光晕与血红色猩红腐败微尘交织，35mm胶片摄影，典雅凄美的暗黑奇幻电影画面。'
    },
    {
        'id': '05_radahn',
        'name': '碎星将军 拉塔恩 (Starscourge Radahn)',
        'target_file': '05_radahn_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的碎星将军拉塔恩（Starscourge Radahn）。一位体型巨大如巨人的战神将领，身披厚重赤金狮子重铠与红色鬃毛头盔，背负两柄巨型黑石碎星重剑。他坐在矮小的爱马白毛战马背上，屹立在狂风呼啸的血红色荒凉沙丘上。深邃的夜空中繁星闪烁，紫色重力魔法微光在铠甲与剑刃周围隐隐流动。真实的风蚀金属磨损、粗糙沙尘颗粒感，大气磅礴的史诗电影实景剧照。'
    },
    {
        'id': '06_ranni',
        'name': '月之公主 菈妮 (Ranni the Witch)',
        'target_file': '06_ranni_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的魔女菈妮（Ranni the Witch）。一位拥有四条手臂的冷艳人偶魔女，面部呈现出极其逼真温润的白瓷人偶质感，眼旁伴随着半透明幽蓝色的第二重灵魂面容。她头戴一顶宽檐大尖顶白雪魔女帽，身裹毛茸茸的厚重雪白皮草斗篷。在清冷幽静的石塔阳台上，她四手交叠托着一枚散发暗冷银光的暗月戒指，身后是浩瀚幽蓝的夜空与一轮巨大的暗月。神秘、空灵、高贵，电影质感。'
    },
    {
        'id': '07_rennala',
        'name': '满月女王 蕾娜菈 (Rennala, Queen of the Full Moon)',
        'target_file': '07_rennala_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的满月女王蕾娜菈（Rennala, Queen of the Full Moon）。雷亚卢卡利亚大书库的水面幻境中，一位高挑优雅的成年女性学者女王，佩戴高耸的银色新月形头冠，身穿深靛蓝色天鹅绒丝绸长袍。她赤足轻踏在倒映着繁星与巨大发光满月的平静水面上，怀中轻拥一枚散发温润琥珀金光的巨大琥珀卵。周围漂浮着微弱的蓝色辉石魔法星光，神秘清冷，绝美的电影实拍质感。'
    },
    {
        'id': '08_margit',
        'name': '恶兆妖鬼 玛尔基特 (Margit, the Fell Omen)',
        'target_file': '08_margit_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的恶兆妖鬼玛尔基特（Margit, the Fell Omen）。在狂风呼啸的史东薇尔城悬崖石桥上，一位佝偻而高大威严的恶兆老者。他头上盘根错节生长着狰狞的天然角质角枝，身裹破烂褴褛的灰黄色粗布斗篷，手握一根粗粝沉重的古木杖，另一手正凝聚出一柄半透明的黄金光芒匕首。暴风雨前夕的阴暗天空，飞沙走石，粗糙逼真的皮肤纹理与角质层，吉尔莫·德尔·托罗风格奇幻电影剧照。'
    },
    {
        'id': '09_maliketh',
        'name': '黑剑 玛利喀斯 (Maliketh, the Black Blade)',
        'target_file': '09_maliketh_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中的“黑剑”玛利喀斯（Maliketh, the Black Blade）。在逐渐崩解的风暴神殿渐毁的法姆·亚兹拉悬浮巨石之间，一位凶猛敏捷的黑兽野兽战士。身披刻满符文的黑曜石与黄金嵌条铠甲，银白色的粗糙兽毛在狂风中倒竖。双手挥舞着一柄巨大的黑色双手重剑，剑刃缠绕着致命的暗红与黑色命定之死火焰。周围碎石漂浮，风暴雷霆环绕，极致写实的物理材质与火光映射，暗黑史诗电影巨作。'
    },
    {
        'id': '10_limgrave_erdtree',
        'name': '宁姆格福与黄金树远景 (Limgrave & Erdtree Vista)',
        'target_file': '10_limgrave_erdtree_liveaction.png',
        'prompt': '请用DALL-E生成一张电影级真人实景照片：艾尔登法环中退色者最初踏足的宁姆格福引导之始远景（Limgrave Vista）。站在开满黄色小花的青葱海边悬崖草甸上，俯瞰辽阔的交界地大地。远方高耸的山崖上坐落着古老灰白色的史东薇尔要塞城堡，而在整片大地正中央，那株冲破云霄、通体散发出神圣柔和琥珀金光的宏伟黄金树屹立在大地上，金色光斑透过薄雾洒向大地。35mm广角电影胶片，真实绝美的奇幻风光摄影。'
    }
]

def generate_one(task):
    target_path = os.path.join(OUTPUT_DIR, task['target_file'])
    if os.path.exists(target_path) and os.path.getsize(target_path) > 100000:
        print(f"[{task['id']}] Already exists ({os.path.getsize(target_path)/1024:.1f} KB), skipping.")
        return True

    print(f"\n==========================================", flush=True)
    print(f"Starting [{task['id']}] - {task['name']}", flush=True)
    print(f"==========================================", flush=True)

    before_files = set(glob.glob(os.path.join(OUTPUT_DIR, '*.png')))

    cmd = [
        'opencli', 'chatgpt', 'image',
        task['prompt'],
        '--op', OUTPUT_DIR,
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

    after_files = set(glob.glob(os.path.join(OUTPUT_DIR, '*.png')))
    new_files = list(after_files - before_files)

    if new_files:
        newest = sorted(new_files, key=lambda f: os.path.getmtime(f), reverse=True)[0]
        os.rename(newest, target_path)
        print(f"SUCCESS: Saved as {task['target_file']} ({os.path.getsize(target_path)/1024:.1f} KB)", flush=True)
        return True
    else:
        # Check if chatgpt_* files were created
        chatgpt_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, 'chatgpt_*.png')), key=lambda f: os.path.getmtime(f), reverse=True)
        if chatgpt_files:
            latest = chatgpt_files[0]
            os.rename(latest, target_path)
            print(f"SUCCESS (from latest chatgpt_*): Saved as {task['target_file']} ({os.path.getsize(target_path)/1024:.1f} KB)", flush=True)
            return True
        print(f"ERROR: No new image detected for {task['id']}", flush=True)
        return False

def main():
    success_count = 0
    for task in TASKS:
        for attempt in range(2):
            if generate_one(task):
                success_count += 1
                time.sleep(3)
                break
            else:
                print(f"Retrying {task['id']} (attempt {attempt+2})...", flush=True)
                time.sleep(5)

    print(f"\nAll tasks finished! {success_count}/{len(TASKS)} images generated successfully.", flush=True)

if __name__ == '__main__':
    main()
