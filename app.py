import gradio as gr
import os

def get_path(rel_path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), rel_path))

with gr.Blocks() as demo:
    gr.Markdown("# Seismology Raspberry Pi Project")
    
    with gr.Tab("使用過程"):
        gr.Markdown("""
        ### 過程
        MobaXterm中的SSH可以連接網路，利用Raspberry Pi的USB接頭連接手機網路後就可以無線操作。
        
        ### 接線過程
        電路板與麵包板的接線方式：電路板連接電源輸出和接地線(避免燒焦)；電路板感應三軸加速度，可以將訊息傳遞給Raspberry Pi；麵包板連接LED燈與蜂鳴器，當檢測器感應到晃動時傳遞給Raspberry Pi，將感應結果傳遞到LED燈與蜂鳴器，類似發出警報功能。
        """)
        with gr.Row():
            gr.Image(get_path("tools/107371_0.jpg"), label="接線圖片一")
            gr.Image(get_path("tools/107372_0.jpg"), label="接線圖片二")
            gr.Image(get_path("tools/107373_0.jpg"), label="接線圖片三")
            gr.Image(get_path("tools/107376.jpg"), label="接線圖片四")
        
    with gr.Tab("結果圖片"):
        gr.Markdown("""
        ### 結果
        MobaXterm有連接Discord的功能，可以利用此特性用python寫發出警報通知傳到Discord，並且上傳繪圖功能，像是特定時間內發生的加速度(圖一)、最大合成加速度的合力方向(圖二)、以及監測出地震強度的能力(圖三)。
        """)
        with gr.Row():
            gr.Image(get_path("results/trend_chart.png"), label="圖一: 特定時間內發生的加速度")
            gr.Image(get_path("results/vector_3d_chart.png"), label="圖二: 最大合成加速度的合力方向")
            gr.Image(get_path("results/未命名.png"), label="圖三: 監測出地震強度的能力")
            
    with gr.Tab("影片結果"):
        gr.Markdown("### 影片結果展示")
        with gr.Row():
            gr.Video(get_path("video/9af0f7b0-ff20-4b93-bfdb-c236b2be918a.mp4"), label="影片一")
            gr.Video(get_path("video/abdc8735-dba1-47ec-bd87-5a23c7433095.mp4"), label="影片二")

if __name__ == "__main__":
    demo.launch()
