import gradio as gr
from df.enhance import enhance, init_df, load_audio, save_audio
from df.utils import download_file

def transform_audio(audio_file):
    print(audio_file)
    model, df_state, _ = init_df()
    audio, _ = load_audio(audio_file, sr=df_state.sr())
    enhanced = enhance(model, df_state, audio)
    save_audio(audio_file.replace(".wav","_output.wav"), enhanced, df_state.sr())
    return audio_file.replace(".wav","_output.wav")

gr.Interface(
    fn=transform_audio,
    inputs=[
        gr.Audio(sources="upload", type="filepath", label="Upload Audio File")
    ],
    outputs=gr.Audio(label="Denoised audio"),
    title="DeepFilterNet Web UI",
    description="A simple web UI built in Gradio for audio denoising with DeepFilterNet.",
    live='true'
).launch(inbrowser='true')
