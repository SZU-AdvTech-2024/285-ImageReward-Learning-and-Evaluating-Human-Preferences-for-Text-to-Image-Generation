from ImageReward import ReFL_

if __name__ == "__main__":
    args = ReFL_.parse_args()
    trainer = ReFL_.Trainer("CompVis/stable-diffusion-v1-4", "data/refl_data.json", args=args)
    trainer.train(args=args)
    # # os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
    # prompt = "a painting of an ocean with clouds and birds, day time, low depth field effect"
    # img_prefix = "assets/images"
    # generations = [f"{pic_id}.webp" for pic_id in range(1, 5)]
    # img_list = [os.path.join(img_prefix, img) for img in generations]
    # model = RM.load("ImageReward-v1.0")
    # with torch.no_grad():
    #     ranking, rewards = model.inference_rank(prompt, img_list)
    #     # Print the result
    #     print("\nPreference predictions:\n")
    #     print(f"ranking = {ranking}")
    #     print(f"rewards = {rewards}")
    #     for index in range(len(img_list)):
    #         score = model.score(prompt, img_list[index])
    #         print(f"{generations[index]:>16s}: {score:.2f}")