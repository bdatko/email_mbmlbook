from pathlib import Path
from typing import Union

import pandas as pd
from tqdm import tqdm
import fire

import email_mbmlbook


def str_to_path(path: str):
    return path if isinstance(path, Path) else Path(path)


def save_data(path: Union[Path, str]):
    path = str_to_path(path)
    for filename, args in tqdm(email_mbmlbook.FILES.items()):
        data = []
        for xml, user_feature_set in zip(args["xml"], args["user_feature_set"]):
            data_xml = email_mbmlbook.FeatureSet(
                xml, args["datasets"], user_feature_set
            )
            data.append(data_xml.to_pandas())
        if len(data) == 1:
            res = data[0]
        else:
            res = pd.concat(data)
            res.reset_index(inplace=True, drop=True)

        res.to_csv(path / filename, index=False)


if __name__ == "__main__":
    fire.Fire(
        {
            "save_data": save_data,
        }
    )
