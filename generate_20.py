import subprocess
import os
import time
import glob
import sys

OUTPUT_DIR = '/Users/sym/code/elden_ring_liveaction/v2_20_gallery'
os.makedirs(OUTPUT_DIR, exist_ok=True)

TASKS = [
    # 1. 梅琳娜
    {
        'id': '01_melina',
        'name': '梅琳娜 (Melina, Kindling Maiden)',
        'target_file': '01_melina_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机实拍的真实人类照片：扮演《艾尔登法环》梅琳娜（Melina）的真实年轻女性特写肖像。纯相机实拍风格，极度写实的真人活人感，像用佳能EOS R5搭配85mm f/1.4镜头在黄昏户外拍摄的真实人像。一位20岁出头的清秀女性，面部呈现完全未修图的自然人类皮肤质感，细腻毛孔、微小面部纹理与自然的唇纹清晰可见。她左眼紧闭且眼角带有逼真的人类皮肤刺青淡痕，右侧睁开的金色眼睛流转着真实人类眼眸的润泽光采与柔和神性。棕色短发在夕阳微风中有些许自然的凌乱碎发。她身披粗糙做旧的暗墨绿色厚羊毛旅行斗篷，内搭风化亚麻长袍，颈间戴着真实的金色金属符节项圈。背景是开满微型野花的宁姆格福黄昏草甸与远处微弱的金色篝火微光。真实的弱光浅景深摄影，没有CG、3D模型或数字绘画感，完全是一张真实生活中的人物实拍照片。'
    },
    # 2. “白面具”梵雷
    {
        'id': '02_varre',
        'name': '“白面具”梵雷 (White Mask Varré)',
        'target_file': '02_varre_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机抓拍的真实人类照片：扮演《艾尔登法环》“白面具”梵雷（White Mask Varré）的真实男性肖像。纯相机实拍风格，极度写实的活人感，像用索尼A7R5单反在阳光明媚的荒野拍摄的人物纪实。一位30多岁、面带嘲弄与审视微笑的优雅欧洲男性，有着自然的胡茬微影与眼角细纹，活人眼神阴鸷狡黠。他单手把一枚略带做旧裂痕与干涸血迹的苍白陶瓷外科军医面具轻轻掀开到脸庞一侧，露出真实的皮肤毛孔与血色。身穿一件手工缝制但沾染斑驳暗红血渍与尘土的米白色外科医师长风衣，戴着深红色皮革手套。背景是阳光照射下开满黄花的草甸与石制残垣，真实的户外明亮阳光与自然光影折射，绝对无CG假面或插画感，极其生动逼真的活人抓拍。'
    },
    # 3. “煮虾哥”布莱格
    {
        'id': '03_boggart',
        'name': '“煮虾哥”布莱格 (Blackguard Big Boggart)',
        'target_file': '03_boggart_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机抓拍的真实人类照片：扮演《艾尔登法环》流氓“煮虾哥”布莱格（Blackguard Big Boggart）的真实中年男子肖像。极度写实的真人活人感，像国家地理摄影师抓拍的市井铁匠或渔民生活照。一位40多岁体格粗壮、满脸胡茬与沧桑风霜痕迹的中年硬汉，皮肤粗糙带有真实的汗渍、油烟黑灰与晒斑，眼神粗鲁却带着烟火气的实在感。他头戴一顶向后推起的沉重做旧铁锅水壶头盔，身穿磨损严重的厚皮围裙与布满油污的粗麻衬衣，正坐在一只旧木桶上，手里用粗糙的大手抓着一只刚从滚烫铁锅里捞出来的煮红大鳌虾大快朵颐。身后是一口架在柴火上冒着滚滚白色热汽的铸铁大锅，湿漉漉的湖区湿地破木屋背景。真实的生活呼吸感与环境光线，毫无CG与磨皮假面。'
    },
    # 4. 铁拳亚历山大与流浪旅行者
    {
        'id': '04_alexander',
        'name': '铁拳亚历山大与流浪旅行者 (Iron Fist Alexander)',
        'target_file': '04_alexander_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机实拍的真实探险抓拍照片：一位真实的旅行者在野外峡谷中偶遇《艾尔登法环》中标志性的战士壶“铁拳亚历山大”（Iron Fist Alexander）。纯相机实拍风格，极度写实的现场感。前景是一位身穿磨损皮革护甲与旅行披风的真实年轻探险家，正半蹲在泥土坑旁，手扶着这只巨大的古陶壶。战士壶是一个直径两米多的纯物理实物道具古陶瓮，表面有着极其真实的粗陶陶土质感、斑驳青苔、开裂后用古代金色漆修补的金缮缝隙，以及顶部的红色封蜡印记。周围是秋天枯黄的杂草、湿润的黑泥与碎石。真实的自然阴天光线，浅景深虚化，真实的相机镜头质感，绝对没有3D建模或二次元数码感，像一张电影拍摄现场的真实花絮照片。'
    },
    # 5. “半狼”布莱泽
    {
        'id': '05_blaidd',
        'name': '“半狼”布莱泽 (Blaidd the Half-Wolf)',
        'target_file': '05_blaidd_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在冷色月光下实拍的真实特技演员照片：扮演《艾尔登法环》“半狼”布莱泽（Blaidd the Half-Wolf）的高大战士。极度写实的纯相机实拍风格，由高大魁梧的特技演员佩戴极其逼真的手工定制狼首特效妆容与长毛兽首头套。深灰色的浓密粗糙狼毛在冷风中根根分明，呼出的热气在夜间冷风中化作白雾，一双充满野性与忠诚的人类神采眼眸在毛发下真实凝视。他身披厚重的手工锻造做旧精钢板甲与撕裂的粗皮披风，肩头扛着一柄巨大沉重的双手骑士大剑。站在迷雾森林深处的古老石砌废墟高台上，清冷月光照亮甲片上的锈迹与划痕。真实的夜景长焦摄影，完全剔除CG渲染感，极具震撼的实物道具与活人生动感。'
    },
    # 6. 死眠少女 菲雅
    {
        'id': '06_fia',
        'name': '死眠少女 菲雅 (Fia, Deathbed Companion)',
        'target_file': '06_fia_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机室内微光实拍的真实女性肖像：扮演《艾尔登法环》死眠少女菲雅（Fia）的真实活人女性特写。极度写实的真人活人感，像用哈苏中画幅相机在烛光卧室拍摄的真实人像。一位20多岁面容苍白温婉、带着深沉母性与哀伤眼神的真实年轻女性，面部完全未修图，有着极其细腻真实的自然皮肤毛孔、锁骨处真实的皮肤光泽与自然的浅淡唇纹。她身穿一袭厚重柔软的深黑色天鹅绒连帽哀悼长裙，兜帽下露出一缕柔顺的金棕色发丝。她正坐在古老雕花木床边，双臂温柔地环抱并安抚着怀中的旅人，真实的人类双手骨节分明且指尖泛白。房间角落点燃的真实白蜡烛散发温暖微弱的光芒，照亮墙面石砖纹理。绝无CG、塑料假面或数字绘画痕迹，纯正高格调人像摄影。'
    },
    # 7. 盲女海妲
    {
        'id': '07_hyetta',
        'name': '盲女海妲 (Hyetta, Maiden of the Three Fingers)',
        'target_file': '07_hyetta_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机实拍的真实年轻女性肖像：扮演《艾尔登法环》盲女海妲（Hyetta）的真实人类面容。纯相机实拍风格，极度写实的活人感。一位清瘦素净的20岁年轻女孩，双眼缠着一条粗糙做旧、泛黄磨损的亚麻布眼罩，面颊白皙自然，有着未经修饰的毛孔、微小雀斑与略带脱皮干涸的真实嘴唇，神情展现出盲人特有的专注、天真与对神圣热望的脆弱活人感。她身穿一件带有粗粝手工针脚的米白色粗麻修女服，微微颤抖的双手捧着一枚散发温和暗金色黄光的“夏玻利利葡萄”果实道具。背景是利耶尼亚湖区阴雨连绵的青苔岩石与水洼，柔和阴雨天散射光线，真实的浅景深特写，毫无CG与二次元假感，充满情感张力的人像实拍。'
    },
    # 8. 金面具
    {
        'id': '08_goldmask',
        'name': '金面具 (Goldmask, the Radiant Transcendence)',
        'target_file': '08_goldmask_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机抓拍的真实苦行僧照片：扮演《艾尔登法环》金面具（Goldmask）的真实古老智者。极度写实的活人感与现场感。一位身形极度消瘦但充满筋骨力量的老年苦行僧演员，苍老而充满褶皱、青筋与晒斑的真实皮肤裸露在空气中，肋骨与锁骨清晰可见。他面部佩戴着一具由黄铜手工敲击而成、形如绽放向日葵的多层金色光芒面具道具，面具边缘的铜铸光芒在夕阳下泛出柔和金属光晕。他身披一条风化破烂的枯黄色粗布僧袍，静默站在狂风吹拂的古老悬崖石桥边缘，右臂枯瘦如柴的手指正笔直指向金黄色的天空。真实深秋狂风吹动布料，真实的落日斜阳硬光与阴影对比，绝对没有3D建模或数字画感，令人肃然起敬的真实纪实摄影。'
    },
    # 9. 魔法剑士 罗杰尔
    {
        'id': '09_rogier',
        'name': '魔法剑士 罗杰尔 (Sorcerer Rogier)',
        'target_file': '09_rogier_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机拍摄的真实人类肖像：扮演《艾尔登法环》魔法剑士罗杰尔（Sorcerer Rogier）的年轻学者。纯相机实拍风格，极度写实的活人呼吸感。一位面容清瘦英俊但带着病容与疲惫的20多岁青年男子，有着完全未精修的真实皮肤毛孔与熬夜产生的暗淡眼圈，眼神却依旧保持着学者的温润与谦逊。他头戴一顶标志性的夸张宽檐墨绿色羊毛毡大帽子，上面插着一根华贵的长羽毛，身穿深蓝色丝绒与粗呢拼接的学者旅行袍。他坐在圆桌厅堂的石砌回廊墙角，双腿盖着厚厚的粗羊毛保暖毛毯，手边斜靠着一柄纤细优美的实物银色刺剑，剑柄镶嵌的蓝色辉石泛出微弱天然矿石光泽。温暖微暗的室内烛光人像摄影，真实生活感，完全摒弃任何CG和数字绘画感。'
    },
    # 10. “战鬼”巴格莱姆 (圆桌骑士套装)
    {
        'id': '10_vagram_wolf',
        'name': '“战鬼”巴格莱姆 / 白狼骑士 (Raging Wolf Tarnished)',
        'target_file': '10_vagram_wolf_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在冷色战场上抓拍的真实人类重装骑士照片：扮演《艾尔登法环》封面标志性白狼骑士“战鬼”巴格莱姆（Raging Wolf Armor）的特技战士。纯相机实拍风格，极度写实的活人感。一位身形魁梧结实的真实战士，全套身穿由冷作锻造的高碳钢与铁皮打造的写实白狼板甲，盔甲表面布满真实的剑击凹痕、金属磨损光泽、烟熏黑渍与干涸泥点，头盔后部装饰着粗糙但真实的白色长马鬃马尾在狂风中猛烈甩动。他单膝跪在灰白色的风化石砖废墟上，一双皮革手套紧握一柄开刃的古旧钢阔剑，下甲裙摆撕裂磨损。背景是阴云密布、飘落细微雨丝与灰烬的荒凉战场，真实的快门凝固飞扬泥水，没有CG模型、无二次元油画感，顶级中世纪冷兵器战争电影实拍剧照。'
    },
    # 11. 初代艾尔登之王 葛孚雷
    {
        'id': '11_godfrey',
        'name': '初代艾尔登之王 葛孚雷 (Godfrey, First Elden Lord)',
        'target_file': '11_godfrey_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机拍摄的真实中老年王者勇士照片：扮演《艾尔登法环》初代艾尔登之王葛孚雷（Godfrey）的健壮演员肖像。纯相机实拍风格，震撼写实的活人感。一位50岁左右身材极为雄壮魁梧的蛮王战士，留着花白粗硬的络腮胡与斑白披肩长发，面部与厚实的胸膛上布满肉眼可见的交错战伤疤痕、皮肤毛孔、真实的汗水反光与沧桑皱纹，一双狮子般威严沧桑的人类眼睛。他肩头披着沉重的白野兽皮毛披肩，身穿带有黄金狮子浮雕但满是刀劈斧凿痕迹的重型古铜板甲，单手握着一柄巨大沉重、斧刃带有深深豁口的旧钢战斧。背景是巨大石柱倒塌的古老王座大殿废墟，穿透残壁的金色斜阳照耀在他苍老坚硬的脸庞上。完全真实的写实肖像摄影，无CG假人、无3D磨皮。'
    },
    # 12. “恶兆王”蒙葛特
    {
        'id': '12_morgott',
        'name': '“恶兆王”蒙葛特 (Morgott, the Omen King)',
        'target_file': '12_morgott_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机实拍的真实悲剧王者照片：扮演《艾尔登法环》“恶兆王”蒙葛特（Morgott, Omen King）的悲怆老者全身肖像。极度写实的纯相机实拍风格。一位高大消瘦而略微佝偻的老年特技演员，头部与肩颈经过好莱坞顶级物理特效化妆，长出自然而粗糙的灰褐色天然角质畸角，角质层纹理如同老树树皮般真实风化。他面容枯槁沧桑，一双混浊而充满忠贞深情的人类眼睛流露出守护黄金树的疲惫与神伤。身上仅裹着破烂粗糙的深黄灰色亚麻破布斗篷，赤足踩在王城罗德尔王座前斑驳开裂的石阶上，粗糙双手拄着一根由天然老树根制作的盘结手杖。微光环境人像摄影，真实的布料纤维与角质反射，毫无CG、3D动画或塑料感，极具莎士比亚悲剧张力的真实抓拍。'
    },
    # 13. “鲜血君王”蒙格
    {
        'id': '13_mohg',
        'name': '“鲜血君王”蒙格 (Mohg, Lord of Blood)',
        'target_file': '13_mohg_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在昏暗地下神殿实拍的真实人物照片：扮演《艾尔登法环》“鲜血君王”蒙格（Mohg, Lord of Blood）的黑暗角质领主。极度写实的真人活人感。一位身形庞大高贵的黑暗君王，头上盘绕着巨大粗糙的天然角质弯角，角尖带有天然生长的骨质凹凸。面容凶戾高傲，双眼在阴影中闪烁着疯狂而狂热的活人神色。他身穿一套由奢华黑色天鹅绒制成、边缘刺绣有繁复金线与暗红宝石饰边的古老帝国礼服，肩挂厚重黑铁护肩，双手紧握着一柄铸铁打造、带有暗红金属光泽与铁锈沉淀的巨大三叉血戟。地下神殿背景中数百根真实红蜡烛熊熊燃烧，跳跃的真实烛火映照在天鹅绒面料与冰冷金属戟尖上。绝非数字CG渲染，纯正大画幅暗调舞台摄影风格。'
    },
    # 14. “接肢”葛瑞克
    {
        'id': '14_godrick',
        'name': '“接肢”葛瑞克 (Godrick the Grafted)',
        'target_file': '14_godrick_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机实拍的真实疯癫领主照片：扮演《艾尔登法环》“接肢”葛瑞克（Godrick the Grafted）的真实贵族老者肖像。纯相机实拍风格，极度写实的活人感。一位60岁左右身躯异常庞大臃肿、面容衰老畸变的落魄君王，稀疏花白的金发贴在满是冷汗与污垢的额头上，眼睛布满血丝，嘴角泛着神经质而狂妄自大的神经质笑容，皮肤上的老年斑、深邃法令纹与松弛下颌皮肤细节极其真实。他身上胡乱披挂着数件沾满灰尘的华贵金色刺绣紫红丝绒王袍，右臂套装着一个由真实工匠制作的做旧炭化龙头骨喷火器模型道具，牙齿狰狞，骨质焦黑。背景是史东薇尔城堡断壁残垣的中庭泥泞地面，真实的阴冷自然光线与扬尘空气。绝无3D平滑CG感，令人毛骨悚然的写实人物肖像。'
    },
    # 15. “穿刺者”梅瑟莫 (黄金树幽影)
    {
        'id': '15_messmer',
        'name': '“穿刺者”梅瑟莫 (Messmer the Impaler)',
        'target_file': '15_messmer_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机实拍的真实反派人物肖像：扮演《艾尔登法环：黄金树幽影》“穿刺者”梅瑟莫（Messmer the Impaler）的真实高挑青年男子。纯相机实拍风格，极度写实的活人感。一位身材修长偏瘦、面色苍白如纸的20多岁欧洲青年演员，面容清冷阴郁，完全未精修的真实皮肤毛孔与深邃锁骨，左眼皮紧合带有蛇鳞般的细微皮肤纹理，右眼深邃而冰冷。他有着一头被风吹乱的鲜艳火红长发，身穿暗沉做旧的黑红黄铜鳞甲与一条粗糙破损的红色毛呢披肩。他坐在一张高耸阴森的黑铁王座上，单手持着一柄锋利修长的双刃刺矛道具，矛尖闪烁着真实的暗红色余烬炭火微光。背景是幽影之地燃烧着暗火的古老石厅，真实的环境弱光与微风扬尘，彻底剔除CG与动漫感，极具压迫感的真实人像摄影。'
    },
    # 16. 圣树骑士 罗蕾塔
    {
        'id': '16_loretta',
        'name': '圣树骑士 罗蕾塔 (Royal Knight Loretta)',
        'target_file': '16_loretta_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机夜景实拍的真实女性骑士照片：扮演《艾尔登法环》圣树骑士罗蕾塔（Royal Knight Loretta）的真实女性重骑兵。纯相机实拍风格，极度写实的活人感。一位身姿挺拔威严的女骑士特技演员，端坐在一匹高大强健的真实白色骏马背上。她身穿由精钢与镀银合金打造的卡利亚风格全套骑兵板甲，金属表面有着真实的夜光反光与手工打磨划痕，修长手掌戴着坚实铁手套，握着一柄长达三米的做旧金属战戟，戟尖镶嵌的蓝色宝石在冷月下泛出微弱光芒。战马马蹄轻踏在卡利亚庄园泛起微弱涟漪的浅水池塘中，溅起真实晶莹的水滴。背景是清冷月夜下的古老城堡残垣与松柏树林，真实的相机快门长曝光感，完全排除任何CG模型与数字插画质感。'
    },
    # 17. 史东薇尔城 悬崖外墙与探险者
    {
        'id': '17_stormveil_cliff',
        'name': '史东薇尔城 悬崖外墙与探险者 (Stormveil Castle Cliffside)',
        'target_file': '17_stormveil_cliff_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机抓拍的暴风雨探险真实照片：一位真实的退色者探险家在狂风暴雨中攀爬《艾尔登法环》史东薇尔城海边悬崖栈道。纯相机实拍风格，极度震撼的现场纪实感。前景是一位穿着浸透雨水的厚牛皮短甲与粗铁锁子甲的真实男性背包客探险家，湿透的黑色发丝紧贴额头，脸上满是真实冰冷的雨水珠与疲惫紧绷的表情，双手死死抓住被海水侵蚀的古老风化木栈道护栏。背景是垂直落差百米的险峻海蚀黑石悬崖，下方是汹涌翻滚、撞击出白色浪花的波涛大海，上方是阴沉雷暴云层中巍峨耸立的古老灰石要塞城堡。镜头上带有逼真的真实雨水飞溅微滴与狂风带来的动态模糊，绝非CG渲染与绿幕合成，充满生理窒息感的真实冒险实拍照。'
    },
    # 18. 魔法学院 雷亚卢卡利亚 水上墓地
    {
        'id': '18_raya_lucaria_graveyard',
        'name': '魔法学院 水上墓地与学者 (Raya Lucaria Graveyard)',
        'target_file': '18_raya_lucaria_graveyard_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机在晨雾中抓拍的真实学者探秘照片：两位身穿学院法袍的真实探险学者正行走在《艾尔登法环》雷亚卢卡利亚学院水上墓地中。纯相机实拍风格，极度写实的现场感。前景一位学者手提一盏散发微弱暖黄烛光的黄铜旧马灯，身上的深靛蓝色粗毛呢学者长袍下摆沾满了潮湿的青苔泥水与湖水，背影真实自然；另一位学者正弯腰查看一座被湿地藤蔓缠绕的雕花古墓石碑。周围是弥漫在及膝浅水水面上的浓重湿冷晨雾，水草丛生，数株散发着微弱冷蓝色荧光的托莉娜睡莲在水洼中真实绽放。远处哥特式学院尖顶在白茫茫的晨雾中若隐若现。真实的自然散射柔光，镜头空气透视真实细腻，没有任何CG与电脑绘图痕迹，极具神秘氛围的纪实摄影。'
    },
    # 19. 希芙拉河 地下星空与行者
    {
        'id': '19_siofra_river',
        'name': '希芙拉河 地下星空与行者 (Siofra River Underground)',
        'target_file': '19_siofra_river_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机长曝光实拍的真实探险照片：一位真实的流浪骑士站在《艾尔登法环》希芙拉河地下深处废墟高台上仰望壮丽地下星空。纯相机实拍风格，极度写实的活人感与现场感。画面前景是一位身穿做旧皮毛护具、背负包裹与古旧圆盾的真实背包探险者背影，真实的头发与衣角在地下微风中轻轻拂动。他站在长满发光杂草与风化碎石的古希腊风格巨大石柱基座上。头顶高耸无际的地下洞顶上，数以亿计的发光发光微生物与蓝色星光结晶如同一整片绚烂深邃的紫罗兰色银河星海，柔和清冽的冷蓝辉光映照在下方缓缓流淌的清澈地下河水与巨大古代渡槽废墟上。真实的夜景大光圈长曝光摄影，空气中微弱的灰尘星斑微粒真实可见，毫无CG假光与游戏引擎建模感。'
    },
    # 20. 法姆·亚兹拉的崩解风暴
    {
        'id': '20_farum_azula',
        'name': '法姆·亚兹拉的崩解风暴 (Crumbling Farum Azula)',
        'target_file': '20_farum_azula_realhuman.png',
        'prompt': '请用DALL-E生成一张用单反相机高速快门抓拍的真实末日风暴实景照片：一位身穿重甲的真实骑士在《艾尔登法环》法姆·亚兹拉悬浮崩解巨石桥上艰难前行。纯相机实拍风格，极度写实的现场感。前景是一位体格沉重的真实重甲骑士侧影，他正顶着迎面而来的恐怖狂风艰难弯腰迈步，双手紧握沉重的锻铁大盾护住身前，防风斗篷在狂风中撕扯成破条剧烈甩动，铠甲缝隙中溅入细碎的风化沙砾与尘暴。中景与远景是悬浮在千米风暴高空中的崩塌古代龙神殿废墟巨柱与断桥，天空中是遮天蔽日、电闪雷鸣的巨大漏斗状风暴气旋，金色与赤黑色的雷光在乌云深处隐现。高速相机快门精准抓拍到空气中飞舞的真实碎石颗粒与尘土轨迹，极度逼真的物理光学快门质感，彻底消除3D特效假感，震撼人心的史诗级实景摄影。'
    }
]

def generate_one(task):
    target_path = os.path.join(OUTPUT_DIR, task['target_file'])
    if os.path.exists(target_path) and os.path.getsize(target_path) > 100000:
        print(f"[{task['id']}] Already exists ({os.path.getsize(target_path)/1024:.1f} KB), skipping.", flush=True)
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
    print(f"All tasks finished! {success_count}/{total} images generated successfully.", flush=True)
    print(f"==========================================", flush=True)

if __name__ == '__main__':
    main()
