from glsm.non_predictive.features import OptionsDataFrame
import pytest
from pydantic import ValidationError


def test_options_data_frame_instance(options_data_frame_instances):
    options_df_pass = options_data_frame_instances[0]
    options_df_fail_values = options_data_frame_instances[1]
    options_df_fail_missing_field = options_data_frame_instances[2]

    # Pass
    # Convert each row of the DataFrame to a dictionary and create OptionsDataFrame instances
    [OptionsDataFrame(**row._asdict()) for row in options_df_pass.itertuples(index=False)]

    # Fail values
    with pytest.raises(ValidationError):
        [OptionsDataFrame(**row._asdict()) for row in options_df_fail_values.itertuples(index=False)]

    # Fail missing field
    with pytest.raises(ValidationError):
        [OptionsDataFrame(**row._asdict()) for row in options_df_fail_missing_field.itertuples(index=False)]
