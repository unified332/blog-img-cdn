import os

URLS = \
[
        "https://media.discordapp.net/attachments/1481925633909985370/1481925634547781704/image.png?ex=69cc288c&is=69cad70c&hm=85548ef0c9ef629ecd10b1dc98d10227934d3980df7dada31b0ccfe4bbdd9846&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481925748481720361/image.png?ex=69cc28a7&is=69cad727&hm=3a45ec118082ebc1b2eec005f38e1828a63ce2cf054bde8974beed7a8c8b857c&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481925921383514205/image.png?ex=69cc28d0&is=69cad750&hm=9618b8ca7ff56482e66b7ad80b1204147bec07a83982c9051472cc232e07c060&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481925984486821908/image.png?ex=69cc28df&is=69cad75f&hm=5d57cb9fa5fdf4751dfdf61bf1cff2734eee85ae42b9dd3916be3a20f49a575c&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926096944365608/image.png?ex=69cc28fa&is=69cad77a&hm=ff1c5a6d8eb2061a53e384b9aaacf56790220f8ab149e8355c3b60da28fd9be0&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926236493185105/image.png?ex=69cc291b&is=69cad79b&hm=640ccd4dee3fa8cd76a9be0ca24813813dcccc2cc4d2818b6676881cb72e8bf1&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926319360049273/image.png?ex=69cc292f&is=69cad7af&hm=11a3beaa1635250c0137628e7f19b1843626ada6fe7882234e487ef6cc53c4bd&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926487752839211/image.png?ex=69cc2957&is=69cad7d7&hm=e99af08db171ac5c1189954bcd60359069eb3926c8c1b1133a4794d733e58fae&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926611279413390/image.png?ex=69cc2974&is=69cad7f4&hm=476648bb75e1c58b7a3a0796771f0e0f374f3b6c815c0a58aabafc6bd47e21a2&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926753399083039/image.png?ex=69cc2996&is=69cad816&hm=8cdf5bbaec5071a2ffabb81b23b459b7dc4f58b99079c09be29eea4c68f53a34&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926823443955752/image.png?ex=69cc29a7&is=69cad827&hm=ad2d6d609d45279e51e38479eb0e498d7e2f37823ac4fc6bbbe0f776baa8377e&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481926908206907543/image.png?ex=69cc29bb&is=69cad83b&hm=838c9cdff8817391b53413e9dc271f79b8c17cb047f8bf080fdafef722678f27&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927022409285723/image.png?ex=69cc29d7&is=69cad857&hm=8e2e9fb85e35262c0f8d864b582b79de01804dfec22f9acafe8c400518599943&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927106899345479/image.png?ex=69cc29eb&is=69cad86b&hm=0f06c70894d0e34672b74493044f1907f945316667ac36181c906f5f2c2c9cd0&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927225233379389/image.png?ex=69cc2a07&is=69cad887&hm=ce02fa4e9dbb3e668bb724830a7c75097e5179f7394cd25f3838ab7c88eeed11&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927549708927106/image.png?ex=69cc2a54&is=69cad8d4&hm=1485ca2f9135023207990387ca75a4d7464db3ec85648ff7fc8829d162b7eb52&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927612845654109/image.png?ex=69cc2a63&is=69cad8e3&hm=ffc1390572cb9905dfbb2513b5637f090e19258b649b14ab6a319a39c0b7471d&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927690289287219/image.png?ex=69cc2a76&is=69cad8f6&hm=5b8e5a7b53a792bb12510091da5e23b7486788f90c9bba25d47b2a65dca6aa98&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927782605783171/image.png?ex=69cc2a8c&is=69cad90c&hm=dd662bfc45404a05e003da76c9b9d968af56fccadc542c4a2baba427e91a5e2a&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927821361414226/image.png?ex=69cc2a95&is=69cad915&hm=4fe132234c21a58d83dee6d96751e03ba3d9347dee23ff9775dbcbf207e92a7a&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481927910695768084/image.png?ex=69cc2aaa&is=69cad92a&hm=8aa3e63ba5f7c2f70bd7b612452a4e680600644cb220054055bbae82db05a9dc&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481928145757012029/image.png?ex=69cc2ae2&is=69cad962&hm=a242a50f85296bd1373b35ab3614a0b5a6afe46870cff3a0e36f46a842d7f9f3&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481928252871409664/image.png?ex=69cc2afc&is=69cad97c&hm=1e82c7c0d931dee0070f38898e1acaff4d0e078cf3824ea3bb0714bb5761e724&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481940453807886427/image.png?ex=69cb8d99&is=69ca3c19&hm=02c6e74686c2a81cc67cd4eec6a6d5965fe3382fa5922db9187c9a1b6607f358&=&format=webp&quality=lossless",
    "https://media.discordapp.net/attachments/1481925633909985370/1481940706888122398/image.png?ex=69cb8dd5&is=69ca3c55&hm=f8c0663ba644acf189f543e067f0b4f9e8445bb3967cb3866e5f28cacd668097&=&format=webp&quality=lossless"
]

for i in range(len(URLS)):
    os.system(f"wget -O {i+1} \"{URLS[i]}\"")
    #os.system()
