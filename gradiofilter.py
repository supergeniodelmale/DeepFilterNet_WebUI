import gradio as gr
from df.enhance import enhance, init_df, load_audio, save_audio
from df.utils import download_file

# Define the transformation function
def transform_audio(audio_file):
    print(audio_file)
    # Load default model
    model, df_state, _ = init_df()
    audio, _ = load_audio(audio_file, sr=df_state.sr())
    # Denoise the audio
    enhanced = enhance(model, df_state, audio)
    # Save for listening
    save_audio(audio_file.replace(".wav","_output.wav"), enhanced, df_state.sr())
    #audio = load_audio(audio_file.replace(".wav","_output.wav"), sr=df_state.sr())
    return audio_file.replace(".wav","_output.wav")

# Define the UI
gr.Interface(
    fn=transform_audio,
    inputs=[
        gr.Audio(sources="upload", type="filepath", label="Upload Audio File")
    ],
    outputs=gr.Audio(label="Transformed Audio"),
    title="Audio Transformation",
    description="Upload an audio file and apply a transformation.",
    live='true'
).launch(inbrowser='true')