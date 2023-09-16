import os
import PIL
import gradio as gr
from mmagic.apis import MMagicInferencer
import warnings

warnings.filterwarnings("ignore")


class Text_to_image:
    model_list = ['stable_diffusion', 'controlnet', 'disco_diffusion']

    def __init__(self) -> None:
        self.create_ui()

    def create_ui(self):
        with gr.Row():
            with gr.Column():
                select_model = gr.Dropdown(
                    label='Choose a model',
                    elem_id='od_models',
                    elem_classes='select_model',
                    choices=self.model_list,
                    value=self.model_list[0],
                )
            with gr.Column():
                image_input = gr.Image(
                    label='Image',
                    source='upload',
                    elem_classes='input_image',
                    type='filepath',
                    interactive=True,
                    tool='editor',
                )
                text_input = gr.Textbox(
                    label='text prompt',
                    elem_classes='input_text',
                    interactive=True,
                )
                output = gr.Image(
                    label='Result',
                    source='upload',
                    interactive=False,
                    elem_classes='result',
                )
                run_button = gr.Button(
                    'Run',
                    elem_classes='run_button',
                )
                run_button.click(
                    self.inference,
                    inputs=[select_model, image_input, text_input],
                    outputs=output,
                )

    def inference(self, select_model, image_input, text_input):
        from mmagic.apis import MMagicInferencer
        sd_inferencer = MMagicInferencer(model_name=select_model)
        result_out_dir = 'output/sd_res.png'
        sd_inferencer.infer(text=text_input, result_out_dir=result_out_dir)
        return result_out_dir


class Image_to_image():
    model_list = ['pix2pix', 'cyclegan']

    def __init__(self) -> None:
        self.create_ui()

    def create_ui(self):
        with gr.Row():
            with gr.Column():
                select_model = gr.Dropdown(
                    label='Choose a model',
                    elem_id='od_models',
                    elem_classes='select_model',
                    choices=self.model_list,
                    value=self.model_list[0],
                )
            with gr.Column():
                image_input = gr.Image(
                    label='Image',
                    source='upload',
                    elem_classes='input_image',
                    type='filepath',
                    interactive=True,
                    tool='editor',
                )
                output = gr.Image(
                    label='Result',
                    source='upload',
                    interactive=False,
                    elem_classes='result',
                )
                run_button = gr.Button(
                    'Run',
                    elem_classes='run_button',
                )
                run_button.click(
                    self.inference,
                    inputs=[select_model, image_input],
                    outputs=output,
                )

    def inference(self, select_model, image_input):
        result_out_dir = 'output_img.jpg'
        editor = MMagicInferencer(select_model)
        result = editor.infer(img=image_input, result_out_dir=result_out_dir)
        return result_out_dir


class Image_super_resolution():
    model_list = ['esrgan', 'srcnn', 'srgan_resnet', 'edsr',
                  'rdn', 'dic', 'ttsr', 'glean', 'real_esrgan']

    def __init__(self) -> None:
        self.create_ui()

    def create_ui(self):
        with gr.Row():
            with gr.Column():
                select_model = gr.Dropdown(
                    label='Choose a model',
                    elem_id='od_models',
                    elem_classes='select_model',
                    choices=self.model_list,
                    value=self.model_list[0],
                )
            with gr.Column():
                image_input = gr.Image(
                    label='Image',
                    source='upload',
                    elem_classes='input_image',
                    type='filepath',
                    interactive=True,
                    tool='editor',
                )
                output = gr.Image(
                    label='Result',
                    source='upload',
                    interactive=False,
                    elem_classes='result',
                )
                run_button = gr.Button(
                    'Run',
                    elem_classes='run_button',
                )
                run_button.click(
                    self.inference,
                    inputs=[select_model, image_input],
                    outputs=output,
                )

    def inference(self, select_model, image_input):
        result_out_dir = './output/esrgan_res.png'
        editor = MMagicInferencer('esrgan')
        results = editor.infer(img=image_input, result_out_dir=result_out_dir)
        return result_out_dir


if __name__ == '__main__':
    title = 'MMagic Inference Demo'
    with gr.Blocks(analytics_enabled=False, title=title) as demo:
        with gr.Tabs():
            with gr.TabItem('text_to_image'):
                Text_to_image()
            with gr.TabItem('Image_to_image'):
                Image_to_image()
            with gr.TabItem('Image_super_resolution'):
                Image_super_resolution()
                pass

    demo.queue().launch(share=True)
