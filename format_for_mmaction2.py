# Python script to generate an MMaction2 compatible file structure for training/validation
import os
import pandas as pd

from tqdm import tqdm

# Label -> Class num dict.
LABEL_CLASS_DICT = {
    "adjusting glasses": 0,
    "applauding": 1,
    "checking watch": 2,
    "clapping": 3,
    "coughing": 4,
    "cracking neck": 5,
    "fixing hair": 6,
    "looking at phone": 7,
    "massaging neck": 8,
    "opening bottle (not wine)": 9,
    "reading book": 10,
    "rolling eyes": 11,
    "scrubbing face": 12,
    "shaking head": 13,
    "tapping pen": 14,
    "using remote controller (not gaming)": 15,
    "writing": 16,
    "yawning": 17,
}
SPLITS = ["train", "val"]
ROOT_DL = "pt-v1"

def get_video_files(root_dir, video_extensions={'.mp4'}):
    video_files = []
    for filename in tqdm(os.listdir(root_dir), desc=f'Video files in {root_dir}'):
        full_path = os.path.join(root_dir, filename)
        if os.path.isfile(full_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext in video_extensions:
                base = os.path.splitext(filename)[0]
                video_files.append((base, full_path))
    return video_files

if __name__ == '__main__':
    for split in SPLITS:
        print(f"Generating {split}")
        annotations_dir = os.path.relpath(
            os.path.join(ROOT_DL,"annotations","deepmind","kinetics700_2020",
                         f"{'validate' if split == 'val' else split}.csv"))
        topup_dir = os.path.relpath(
            os.path.join(ROOT_DL,"annotations","deepmind_top-up","kinetics700_2020_delta",
                         f"{'validate' if split == 'val' else split}.csv"))
        
        print(f"Annotations path: {annotations_dir}\n{topup_dir}")

        df_annotations = pd.read_csv(annotations_dir)
        df_topup = pd.read_csv(topup_dir)
        df = pd.concat([df_annotations, df_topup], ignore_index=True)

        # Añadir la columna 'class_num' mapeando la columna 'label'
        df["class_num"] = df["label"].map(LABEL_CLASS_DICT)

        # Obtener vídeos
        video_files = get_video_files(os.path.join(ROOT_DL, split))
        video_basenames = {base for base, _ in video_files}
        print(f"{len(video_files)} files found")

        # Generar columna nombre vídeo
        df["video_name"] = df.apply(
            lambda row: f"{row['youtube_id']}_{int(row['time_start']):06d}_{int(row['time_end']):06d}", axis=1
        )

        # Eliminar las entradas del dataframe que no tengan fichero asociado
        df = df[df["video_name"].isin(video_basenames)].copy()
        print(f"{len(df)} videos with annotations for {split} split")

        # Cada línea tendrá el formato: <youtube_id> <class_num>
        with open(f"{split}.txt", "w") as f:
            for _, row in df.iterrows():
                f.write(f"{row['video_name']}.mp4 {int(row['class_num'])}\n")

        print(f"{split.capitalize()} completed!")
