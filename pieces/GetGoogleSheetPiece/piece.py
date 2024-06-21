from domino.base_piece import BasePiece
from .models import InputModel, OutputModel, SecretsModel
import pandas as pd
import gspread
import json
from tempfile import NamedTemporaryFile


class GetGoogleSheetPiece(BasePiece):

    def piece_function(self, input_data: InputModel, secrets_data: SecretsModel):

        service_account = secrets_data.service_account_data
        if isinstance(service_account, str):
            service_account = json.loads(secrets_data.service_account_data)

        with NamedTemporaryFile('w') as tmp:
            json.dump(service_account, tmp)
            tmp.seek(0)
            gc = gspread.service_account(filename=tmp.name)

        # Open the Google Sheet by its title or URL
        spreadsheet = gc.open(input_data.spreadsheet_name)
        worksheet = spreadsheet.get_worksheet(input_data.worksheet_number)
        records = worksheet.get_all_records()
        df = pd.DataFrame.from_records(records)

        print('DF', df.to_dict())
        print('df', df.to_dict(orient='records'))

        return OutputModel(output_data=df.to_dict(orient='records'))

