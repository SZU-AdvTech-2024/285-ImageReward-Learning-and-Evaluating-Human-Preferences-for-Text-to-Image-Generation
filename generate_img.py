

import torch
from diffusers import AutoencoderKL, DDPMScheduler, StableDiffusionPipeline, UNet2DConditionModel

# 加载模型
pipeline = StableDiffusionPipeline.from_pretrained('checkpoint/refl')
prompt = "A painting of a girl walking in a hallway and suddenly finds a giant sunflower on the floor blocking her way"

# 生成图片
images = pipeline(prompt)

# 保存图片
images.save("output.png")

# 生成图片
images = pipeline(prompt)

# 保存图片
images.save("output.png")