from pydantic import BaseModel, Field


class InputModel(BaseModel):
    spreadsheet_name: str = Field(
        title="Spreadsheet Name",
        description="Name of the Google Sheets document"
    )
    worksheet_number: int = Field(
        title="Worksheet Number",
        description="Number of the worksheet in the Google Sheets document."
    )


class OutputModel(BaseModel):
    output_data: list = Field(
        title="Output Data.",
        description="List of records from the Google Sheet."
    )

class SecretsModel(BaseModel):
    service_account_data: str = Field(
        title="Service Account",
        description="Service account JSON data for Google Sheets API. Paste it as a string.",
    )
