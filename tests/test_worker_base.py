# -*- coding: utf-8 -*-



# todo: deactivated test temporarily
# def test_xicclu_is_working_properly(data_files):
#     """testing if ``DisplayCAL.worker_base.Xicclu`` is working properly"""
#     from DisplayCAL import ICCProfile
#     from DisplayCAL.worker_base import Xicclu
#
#     profile = ICCProfile.ICCProfile(profile=data_files["default.icc"].absolute())
#     xicclu = Xicclu(profile, "r", "a", pcs="X", scale=100)
#     assert xicclu() is not None


def test_something():
    """ """

    idata = [
        "100.0 12.5 62.5",
        "100.0 12.5 65.625",
        "100.0 12.5 68.75",
        "100.0 12.5 71.875",
        "100.0 12.5 75.0",
        "100.0 12.5 78.125",
        "100.0 12.5 81.25",
        "100.0 12.5 84.375",
        "100.0 12.5 87.5",
        "100.0 12.5 90.625",
        "100.0 12.5 93.75",
        "100.0 12.5 96.875",
        "100.0 12.5 100.0",
        "100.0 15.625 0.0",
        "100.0 15.625 3.125",
        "100.0 15.625 6.25",
        "100.0 15.625 9.375",
        "100.0 15.625 12.5",
        "100.0 15.625 15.625",
        "100.0 15.625 18.75",
        "100.0 15.625 21.875",
        "100.0 15.625 25.0",
        "100.0 15.625 28.125",
        "100.0 15.625 31.25",
        "100.0 15.625 34.375",
        "100.0 15.625 37.5",
        "100.0 15.625 40.625",
        "100.0 15.625 43.75",
        "100.0 15.625 46.875",
        "100.0 15.625 50.0",
        "100.0 15.625 53.125",
        "100.0 15.625 56.25",
        "100.0 15.625 59.375",
        "100.0 15.625 62.5",
        "100.0 15.625 65.625",
        "100.0 15.625 68.75",
        "100.0 15.625 71.875",
        "100.0 15.625 75.0",
        "100.0 15.625 78.125",
        "100.0 15.625 81.25",
        "100.0 15.625 84.375",
        "100.0 15.625 87.5",
        "100.0 15.625 90.625",
        "100.0 15.625 93.75",
        "100.0 15.625 96.875",
        "100.0 15.625 100.0",
        "100.0 18.75 0.0",
        "100.0 18.75 3.125",
        "100.0 18.75 6.25",
        "100.0 18.75 9.375",
        "100.0 18.75 12.5",
        "100.0 18.75 15.625",
        "100.0 18.75 18.75",
        "100.0 18.75 21.875",
        "100.0 18.75 25.0",
        "100.0 18.75 28.125",
        "100.0 18.75 31.25",
        "100.0 18.75 34.375",
        "100.0 18.75 37.5",
        "100.0 18.75 40.625",
        "100.0 18.75 43.75",
        "100.0 18.75 46.875",
        "100.0 18.75 50.0",
        "100.0 18.75 53.125",
        "100.0 18.75 56.25",
        "100.0 18.75 59.375",
        "100.0 18.75 62.5",
        "100.0 18.75 65.625",
        "100.0 18.75 68.75",
        "100.0 18.75 71.875",
        "100.0 18.75 75.0",
        "100.0 18.75 78.125",
        "100.0 18.75 81.25",
        "100.0 18.75 84.375",
        "100.0 18.75 87.5",
        "100.0 18.75 90.625",
        "100.0 18.75 93.75",
        "100.0 18.75 96.875",
        "100.0 18.75 100.0",
        "100.0 21.875 0.0",
        "100.0 21.875 3.125",
        "100.0 21.875 6.25",
        "100.0 21.875 9.375",
        "100.0 21.875 12.5",
        "100.0 21.875 15.625",
        "100.0 21.875 18.75",
        "100.0 21.875 21.875",
        "100.0 21.875 25.0",
        "100.0 21.875 28.125",
        "100.0 21.875 31.25",
        "100.0 21.875 34.375",
        "100.0 21.875 37.5",
        "100.0 21.875 40.625",
        "100.0 21.875 43.75",
        "100.0 21.875 46.875",
        "100.0 21.875 50.0",
        "100.0 21.875 53.125",
        "100.0 21.875 56.25",
        "100.0 21.875 59.375",
        "100.0 21.875 62.5",
        "100.0 21.875 65.625",
        "100.0 21.875 68.75",
        "100.0 21.875 71.875",
        "100.0 21.875 75.0",
        "100.0 21.875 78.125",
        "100.0 21.875 81.25",
        "100.0 21.875 84.375",
        "100.0 21.875 87.5",
        "100.0 21.875 90.625",
        "100.0 21.875 93.75",
        "100.0 21.875 96.875",
        "100.0 21.875 100.0",
        "100.0 25.0 0.0",
        "100.0 25.0 3.125",
        "100.0 25.0 6.25",
        "100.0 25.0 9.375",
        "100.0 25.0 12.5",
        "100.0 25.0 15.625",
        "100.0 25.0 18.75",
        "100.0 25.0 21.875",
        "100.0 25.0 25.0",
        "100.0 25.0 28.125",
        "100.0 25.0 31.25",
        "100.0 25.0 34.375",
        "100.0 25.0 37.5",
        "100.0 25.0 40.625",
        "100.0 25.0 43.75",
        "100.0 25.0 46.875",
        "100.0 25.0 50.0",
        "100.0 25.0 53.125",
        "100.0 25.0 56.25",
        "100.0 25.0 59.375",
        "100.0 25.0 62.5",
        "100.0 25.0 65.625",
        "100.0 25.0 68.75",
        "100.0 25.0 71.875",
        "100.0 25.0 75.0",
        "100.0 25.0 78.125",
        "100.0 25.0 81.25",
        "100.0 25.0 84.375",
        "100.0 25.0 87.5",
        "100.0 25.0 90.625",
        "100.0 25.0 93.75",
        "100.0 25.0 96.875",
        "100.0 25.0 100.0",
        "100.0 28.125 0.0",
        "100.0 28.125 3.125",
        "100.0 28.125 6.25",
        "100.0 28.125 9.375",
        "100.0 28.125 12.5",
        "100.0 28.125 15.625",
        "100.0 28.125 18.75",
        "100.0 28.125 21.875",
        "100.0 28.125 25.0",
        "100.0 28.125 28.125",
        "100.0 28.125 31.25",
        "100.0 28.125 34.375",
        "100.0 28.125 37.5",
        "100.0 28.125 40.625",
        "100.0 28.125 43.75",
        "100.0 28.125 46.875",
        "100.0 28.125 50.0",
        "100.0 28.125 53.125",
        "100.0 28.125 56.25",
        "100.0 28.125 59.375",
        "100.0 28.125 62.5",
        "100.0 28.125 65.625",
        "100.0 28.125 68.75",
        "100.0 28.125 71.875",
        "100.0 28.125 75.0",
        "100.0 28.125 78.125",
        "100.0 28.125 81.25",
        "100.0 28.125 84.375",
        "100.0 28.125 87.5",
        "100.0 28.125 90.625",
        "100.0 28.125 93.75",
        "100.0 28.125 96.875",
        "100.0 28.125 100.0",
        "100.0 31.25 0.0",
        "100.0 31.25 3.125",
        "100.0 31.25 6.25",
        "100.0 31.25 9.375",
        "100.0 31.25 12.5",
        "100.0 31.25 15.625",
        "100.0 31.25 18.75",
        "100.0 31.25 21.875",
        "100.0 31.25 25.0",
        "100.0 31.25 28.125",
        "100.0 31.25 31.25",
        "100.0 31.25 34.375",
        "100.0 31.25 37.5",
        "100.0 31.25 40.625",
        "100.0 31.25 43.75",
        "100.0 31.25 46.875",
        "100.0 31.25 50.0",
        "100.0 31.25 53.125",
        "100.0 31.25 56.25",
        "100.0 31.25 59.375",
        "100.0 31.25 62.5",
        "100.0 31.25 65.625",
        "100.0 31.25 68.75",
        "100.0 31.25 71.875",
        "100.0 31.25 75.0",
        "100.0 31.25 78.125",
        "100.0 31.25 81.25",
        "100.0 31.25 84.375",
        "100.0 31.25 87.5",
        "100.0 31.25 90.625",
        "100.0 31.25 93.75",
        "100.0 31.25 96.875",
        "100.0 31.25 100.0",
        "100.0 34.375 0.0",
        "100.0 34.375 3.125",
        "100.0 34.375 6.25",
        "100.0 34.375 9.375",
        "100.0 34.375 12.5",
        "100.0 34.375 15.625",
        "100.0 34.375 18.75",
        "100.0 34.375 21.875",
        "100.0 34.375 25.0",
        "100.0 34.375 28.125",
        "100.0 34.375 31.25",
        "100.0 34.375 34.375",
        "100.0 34.375 37.5",
        "100.0 34.375 40.625",
        "100.0 34.375 43.75",
        "100.0 34.375 46.875",
        "100.0 34.375 50.0",
        "100.0 34.375 53.125",
        "100.0 34.375 56.25",
        "100.0 34.375 59.375",
        "100.0 34.375 62.5",
        "100.0 34.375 65.625",
        "100.0 34.375 68.75",
        "100.0 34.375 71.875",
        "100.0 34.375 75.0",
        "100.0 34.375 78.125",
        "100.0 34.375 81.25",
        "100.0 34.375 84.375",
        "100.0 34.375 87.5",
        "100.0 34.375 90.625",
        "100.0 34.375 93.75",
        "100.0 34.375 96.875",
        "100.0 34.375 100.0",
        "100.0 37.5 0.0",
        "100.0 37.5 3.125",
        "100.0 37.5 6.25",
        "100.0 37.5 9.375",
        "100.0 37.5 12.5",
        "100.0 37.5 15.625",
        "100.0 37.5 18.75",
        "100.0 37.5 21.875",
        "100.0 37.5 25.0",
        "100.0 37.5 28.125",
        "100.0 37.5 31.25",
        "100.0 37.5 34.375",
        "100.0 37.5 37.5",
        "100.0 37.5 40.625",
        "100.0 37.5 43.75",
        "100.0 37.5 46.875",
        "100.0 37.5 50.0",
        "100.0 37.5 53.125",
        "100.0 37.5 56.25",
        "100.0 37.5 59.375",
        "100.0 37.5 62.5",
        "100.0 37.5 65.625",
        "100.0 37.5 68.75",
        "100.0 37.5 71.875",
        "100.0 37.5 75.0",
        "100.0 37.5 78.125",
        "100.0 37.5 81.25",
        "100.0 37.5 84.375",
        "100.0 37.5 87.5",
        "100.0 37.5 90.625",
        "100.0 37.5 93.75",
        "100.0 37.5 96.875",
        "100.0 37.5 100.0",
        "100.0 40.625 0.0",
        "100.0 40.625 3.125",
        "100.0 40.625 6.25",
        "100.0 40.625 9.375",
        "100.0 40.625 12.5",
        "100.0 40.625 15.625",
        "100.0 40.625 18.75",
        "100.0 40.625 21.875",
        "100.0 40.625 25.0",
        "100.0 40.625 28.125",
        "100.0 40.625 31.25",
        "100.0 40.625 34.375",
        "100.0 40.625 37.5",
        "100.0 40.625 40.625",
        "100.0 40.625 43.75",
        "100.0 40.625 46.875",
        "100.0 40.625 50.0",
        "100.0 40.625 53.125",
        "100.0 40.625 56.25",
        "100.0 40.625 59.375",
        "100.0 40.625 62.5",
        "100.0 40.625 65.625",
        "100.0 40.625 68.75",
        "100.0 40.625 71.875",
        "100.0 40.625 75.0",
        "100.0 40.625 78.125",
        "100.0 40.625 81.25",
        "100.0 40.625 84.375",
        "100.0 40.625 87.5",
        "100.0 40.625 90.625",
        "100.0 40.625 93.75",
        "100.0 40.625 96.875",
        "100.0 40.625 100.0",
        "100.0 43.75 0.0",
        "100.0 43.75 3.125",
        "100.0 43.75 6.25",
        "100.0 43.75 9.375",
        "100.0 43.75 12.5",
        "100.0 43.75 15.625",
        "100.0 43.75 18.75",
        "100.0 43.75 21.875",
        "100.0 43.75 25.0",
        "100.0 43.75 28.125",
        "100.0 43.75 31.25",
        "100.0 43.75 34.375",
        "100.0 43.75 37.5",
        "100.0 43.75 40.625",
        "100.0 43.75 43.75",
        "100.0 43.75 46.875",
        "100.0 43.75 50.0",
        "100.0 43.75 53.125",
        "100.0 43.75 56.25",
        "100.0 43.75 59.375",
        "100.0 43.75 62.5",
        "100.0 43.75 65.625",
        "100.0 43.75 68.75",
        "100.0 43.75 71.875",
        "100.0 43.75 75.0",
        "100.0 43.75 78.125",
        "100.0 43.75 81.25",
        "100.0 43.75 84.375",
        "100.0 43.75 87.5",
        "100.0 43.75 90.625",
        "100.0 43.75 93.75",
        "100.0 43.75 96.875",
        "100.0 43.75 100.0",
        "100.0 46.875 0.0",
        "100.0 46.875 3.125",
        "100.0 46.875 6.25",
        "100.0 46.875 9.375",
        "100.0 46.875 12.5",
        "100.0 46.875 15.625",
        "100.0 46.875 18.75",
        "100.0 46.875 21.875",
        "100.0 46.875 25.0",
        "100.0 46.875 28.125",
        "100.0 46.875 31.25",
        "100.0 46.875 34.375",
        "100.0 46.875 37.5",
        "100.0 46.875 40.625",
        "100.0 46.875 43.75",
        "100.0 46.875 46.875",
        "100.0 46.875 50.0",
        "100.0 46.875 53.125",
        "100.0 46.875 56.25",
        "100.0 46.875 59.375",
        "100.0 46.875 62.5",
        "100.0 46.875 65.625",
        "100.0 46.875 68.75",
        "100.0 46.875 71.875",
        "100.0 46.875 75.0",
        "100.0 46.875 78.125",
        "100.0 46.875 81.25",
        "100.0 46.875 84.375",
        "100.0 46.875 87.5",
        "100.0 46.875 90.625",
        "100.0 46.875 93.75",
        "100.0 46.875 96.875",
        "100.0 46.875 100.0",
        "100.0 50.0 0.0",
        "100.0 50.0 3.125",
        "100.0 50.0 6.25",
        "100.0 50.0 9.375",
        "100.0 50.0 12.5",
        "100.0 50.0 15.625",
        "100.0 50.0 18.75",
        "100.0 50.0 21.875",
        "100.0 50.0 25.0",
        "100.0 50.0 28.125",
        "100.0 50.0 31.25",
        "100.0 50.0 34.375",
        "100.0 50.0 37.5",
        "100.0 50.0 40.625",
        "100.0 50.0 43.75",
        "100.0 50.0 46.875",
        "100.0 50.0 50.0",
        "100.0 50.0 53.125",
        "100.0 50.0 56.25",
        "100.0 50.0 59.375",
        "100.0 50.0 62.5",
        "100.0 50.0 65.625",
        "100.0 50.0 68.75",
        "100.0 50.0 71.875",
        "100.0 50.0 75.0",
        "100.0 50.0 78.125",
        "100.0 50.0 81.25",
        "100.0 50.0 84.375",
        "100.0 50.0 87.5",
        "100.0 50.0 90.625",
        "100.0 50.0 93.75",
        "100.0 50.0 96.875",
        "100.0 50.0 100.0",
        "100.0 53.125 0.0",
        "100.0 53.125 3.125",
        "100.0 53.125 6.25",
        "100.0 53.125 9.375",
        "100.0 53.125 12.5",
        "100.0 53.125 15.625",
        "100.0 53.125 18.75",
        "100.0 53.125 21.875",
        "100.0 53.125 25.0",
        "100.0 53.125 28.125",
        "100.0 53.125 31.25",
        "100.0 53.125 34.375",
        "100.0 53.125 37.5",
        "100.0 53.125 40.625",
        "100.0 53.125 43.75",
        "100.0 53.125 46.875",
        "100.0 53.125 50.0",
        "100.0 53.125 53.125",
        "100.0 53.125 56.25",
        "100.0 53.125 59.375",
        "100.0 53.125 62.5",
        "100.0 53.125 65.625",
        "100.0 53.125 68.75",
        "100.0 53.125 71.875",
        "100.0 53.125 75.0",
        "100.0 53.125 78.125",
        "100.0 53.125 81.25",
        "100.0 53.125 84.375",
        "100.0 53.125 87.5",
        "100.0 53.125 90.625",
        "100.0 53.125 93.75",
        "100.0 53.125 96.875",
        "100.0 53.125 100.0",
        "100.0 56.25 0.0",
        "100.0 56.25 3.125",
        "100.0 56.25 6.25",
        "100.0 56.25 9.375",
        "100.0 56.25 12.5",
        "100.0 56.25 15.625",
        "100.0 56.25 18.75",
        "100.0 56.25 21.875",
        "100.0 56.25 25.0",
        "100.0 56.25 28.125",
        "100.0 56.25 31.25",
        "100.0 56.25 34.375",
        "100.0 56.25 37.5",
        "100.0 56.25 40.625",
        "100.0 56.25 43.75",
        "100.0 56.25 46.875",
        "100.0 56.25 50.0",
        "100.0 56.25 53.125",
        "100.0 56.25 56.25",
        "100.0 56.25 59.375",
        "100.0 56.25 62.5",
        "100.0 56.25 65.625",
        "100.0 56.25 68.75",
        "100.0 56.25 71.875",
        "100.0 56.25 75.0",
        "100.0 56.25 78.125",
        "100.0 56.25 81.25",
        "100.0 56.25 84.375",
        "100.0 56.25 87.5",
        "100.0 56.25 90.625",
        "100.0 56.25 93.75",
        "100.0 56.25 96.875",
        "100.0 56.25 100.0",
        "100.0 59.375 0.0",
        "100.0 59.375 3.125",
        "100.0 59.375 6.25",
        "100.0 59.375 9.375",
        "100.0 59.375 12.5",
        "100.0 59.375 15.625",
        "100.0 59.375 18.75",
        "100.0 59.375 21.875",
        "100.0 59.375 25.0",
        "100.0 59.375 28.125",
        "100.0 59.375 31.25",
        "100.0 59.375 34.375",
        "100.0 59.375 37.5",
        "100.0 59.375 40.625",
        "100.0 59.375 43.75",
        "100.0 59.375 46.875",
        "100.0 59.375 50.0",
        "100.0 59.375 53.125",
        "100.0 59.375 56.25",
        "100.0 59.375 59.375",
        "100.0 59.375 62.5",
        "100.0 59.375 65.625",
        "100.0 59.375 68.75",
        "100.0 59.375 71.875",
        "100.0 59.375 75.0",
        "100.0 59.375 78.125",
        "100.0 59.375 81.25",
        "100.0 59.375 84.375",
        "100.0 59.375 87.5",
        "100.0 59.375 90.625",
        "100.0 59.375 93.75",
        "100.0 59.375 96.875",
        "100.0 59.375 100.0",
        "100.0 62.5 0.0",
        "100.0 62.5 3.125",
        "100.0 62.5 6.25",
        "100.0 62.5 9.375",
        "100.0 62.5 12.5",
        "100.0 62.5 15.625",
        "100.0 62.5 18.75",
        "100.0 62.5 21.875",
        "100.0 62.5 25.0",
        "100.0 62.5 28.125",
        "100.0 62.5 31.25",
        "100.0 62.5 34.375",
        "100.0 62.5 37.5",
        "100.0 62.5 40.625",
        "100.0 62.5 43.75",
        "100.0 62.5 46.875",
        "100.0 62.5 50.0",
        "100.0 62.5 53.125",
        "100.0 62.5 56.25",
        "100.0 62.5 59.375",
        "100.0 62.5 62.5",
        "100.0 62.5 65.625",
        "100.0 62.5 68.75",
        "100.0 62.5 71.875",
        "100.0 62.5 75.0",
        "100.0 62.5 78.125",
        "100.0 62.5 81.25",
        "100.0 62.5 84.375",
        "100.0 62.5 87.5",
        "100.0 62.5 90.625",
        "100.0 62.5 93.75",
        "100.0 62.5 96.875",
        "100.0 62.5 100.0",
        "100.0 65.625 0.0",
        "100.0 65.625 3.125",
        "100.0 65.625 6.25",
        "100.0 65.625 9.375",
        "100.0 65.625 12.5",
        "100.0 65.625 15.625",
        "100.0 65.625 18.75",
        "100.0 65.625 21.875",
        "100.0 65.625 25.0",
        "100.0 65.625 28.125",
        "100.0 65.625 31.25",
        "100.0 65.625 34.375",
        "100.0 65.625 37.5",
        "100.0 65.625 40.625",
        "100.0 65.625 43.75",
        "100.0 65.625 46.875",
        "100.0 65.625 50.0",
        "100.0 65.625 53.125",
        "100.0 65.625 56.25",
        "100.0 65.625 59.375",
        "100.0 65.625 62.5",
        "100.0 65.625 65.625",
        "100.0 65.625 68.75",
        "100.0 65.625 71.875",
        "100.0 65.625 75.0",
        "100.0 65.625 78.125",
        "100.0 65.625 81.25",
        "100.0 65.625 84.375",
        "100.0 65.625 87.5",
        "100.0 65.625 90.625",
        "100.0 65.625 93.75",
        "100.0 65.625 96.875",
        "100.0 65.625 100.0",
        "100.0 68.75 0.0",
        "100.0 68.75 3.125",
        "100.0 68.75 6.25",
        "100.0 68.75 9.375",
        "100.0 68.75 12.5",
        "100.0 68.75 15.625",
        "100.0 68.75 18.75",
        "100.0 68.75 21.875",
        "100.0 68.75 25.0",
        "100.0 68.75 28.125",
        "100.0 68.75 31.25",
        "100.0 68.75 34.375",
        "100.0 68.75 37.5",
        "100.0 68.75 40.625",
        "100.0 68.75 43.75",
        "100.0 68.75 46.875",
        "100.0 68.75 50.0",
        "100.0 68.75 53.125",
        "100.0 68.75 56.25",
        "100.0 68.75 59.375",
        "100.0 68.75 62.5",
        "100.0 68.75 65.625",
        "100.0 68.75 68.75",
        "100.0 68.75 71.875",
        "100.0 68.75 75.0",
        "100.0 68.75 78.125",
        "100.0 68.75 81.25",
        "100.0 68.75 84.375",
        "100.0 68.75 87.5",
        "100.0 68.75 90.625",
        "100.0 68.75 93.75",
        "100.0 68.75 96.875",
        "100.0 68.75 100.0",
        "100.0 71.875 0.0",
        "100.0 71.875 3.125",
        "100.0 71.875 6.25",
        "100.0 71.875 9.375",
        "100.0 71.875 12.5",
        "100.0 71.875 15.625",
        "100.0 71.875 18.75",
        "100.0 71.875 21.875",
        "100.0 71.875 25.0",
        "100.0 71.875 28.125",
        "100.0 71.875 31.25",
        "100.0 71.875 34.375",
        "100.0 71.875 37.5",
        "100.0 71.875 40.625",
        "100.0 71.875 43.75",
        "100.0 71.875 46.875",
        "100.0 71.875 50.0",
        "100.0 71.875 53.125",
        "100.0 71.875 56.25",
        "100.0 71.875 59.375",
        "100.0 71.875 62.5",
        "100.0 71.875 65.625",
        "100.0 71.875 68.75",
        "100.0 71.875 71.875",
        "100.0 71.875 75.0",
        "100.0 71.875 78.125",
        "100.0 71.875 81.25",
        "100.0 71.875 84.375",
        "100.0 71.875 87.5",
        "100.0 71.875 90.625",
        "100.0 71.875 93.75",
        "100.0 71.875 96.875",
        "100.0 71.875 100.0",
        "100.0 75.0 0.0",
        "100.0 75.0 3.125",
        "100.0 75.0 6.25",
        "100.0 75.0 9.375",
        "100.0 75.0 12.5",
        "100.0 75.0 15.625",
        "100.0 75.0 18.75",
        "100.0 75.0 21.875",
        "100.0 75.0 25.0",
        "100.0 75.0 28.125",
        "100.0 75.0 31.25",
        "100.0 75.0 34.375",
        "100.0 75.0 37.5",
        "100.0 75.0 40.625",
        "100.0 75.0 43.75",
        "100.0 75.0 46.875",
        "100.0 75.0 50.0",
        "100.0 75.0 53.125",
        "100.0 75.0 56.25",
        "100.0 75.0 59.375",
        "100.0 75.0 62.5",
        "100.0 75.0 65.625",
        "100.0 75.0 68.75",
        "100.0 75.0 71.875",
        "100.0 75.0 75.0",
        "100.0 75.0 78.125",
        "100.0 75.0 81.25",
        "100.0 75.0 84.375",
        "100.0 75.0 87.5",
        "100.0 75.0 90.625",
        "100.0 75.0 93.75",
        "100.0 75.0 96.875",
        "100.0 75.0 100.0",
        "100.0 78.125 0.0",
        "100.0 78.125 3.125",
        "100.0 78.125 6.25",
        "100.0 78.125 9.375",
        "100.0 78.125 12.5",
        "100.0 78.125 15.625",
        "100.0 78.125 18.75",
        "100.0 78.125 21.875",
        "100.0 78.125 25.0",
        "100.0 78.125 28.125",
        "100.0 78.125 31.25",
        "100.0 78.125 34.375",
        "100.0 78.125 37.5",
        "100.0 78.125 40.625",
        "100.0 78.125 43.75",
        "100.0 78.125 46.875",
        "100.0 78.125 50.0",
        "100.0 78.125 53.125",
        "100.0 78.125 56.25",
        "100.0 78.125 59.375",
        "100.0 78.125 62.5",
        "100.0 78.125 65.625",
        "100.0 78.125 68.75",
        "100.0 78.125 71.875",
        "100.0 78.125 75.0",
        "100.0 78.125 78.125",
        "100.0 78.125 81.25",
        "100.0 78.125 84.375",
        "100.0 78.125 87.5",
        "100.0 78.125 90.625",
        "100.0 78.125 93.75",
        "100.0 78.125 96.875",
        "100.0 78.125 100.0",
        "100.0 81.25 0.0",
        "100.0 81.25 3.125",
        "100.0 81.25 6.25",
        "100.0 81.25 9.375",
        "100.0 81.25 12.5",
        "100.0 81.25 15.625",
        "100.0 81.25 18.75",
        "100.0 81.25 21.875",
        "100.0 81.25 25.0",
        "100.0 81.25 28.125",
        "100.0 81.25 31.25",
        "100.0 81.25 34.375",
        "100.0 81.25 37.5",
        "100.0 81.25 40.625",
        "100.0 81.25 43.75",
        "100.0 81.25 46.875",
        "100.0 81.25 50.0",
        "100.0 81.25 53.125",
        "100.0 81.25 56.25",
        "100.0 81.25 59.375",
        "100.0 81.25 62.5",
        "100.0 81.25 65.625",
        "100.0 81.25 68.75",
        "100.0 81.25 71.875",
        "100.0 81.25 75.0",
        "100.0 81.25 78.125",
        "100.0 81.25 81.25",
        "100.0 81.25 84.375",
        "100.0 81.25 87.5",
        "100.0 81.25 90.625",
        "100.0 81.25 93.75",
        "100.0 81.25 96.875",
        "100.0 81.25 100.0",
        "100.0 84.375 0.0",
        "100.0 84.375 3.125",
        "100.0 84.375 6.25",
        "100.0 84.375 9.375",
        "100.0 84.375 12.5",
        "100.0 84.375 15.625",
        "100.0 84.375 18.75",
        "100.0 84.375 21.875",
        "100.0 84.375 25.0",
        "100.0 84.375 28.125",
        "100.0 84.375 31.25",
        "100.0 84.375 34.375",
        "100.0 84.375 37.5",
        "100.0 84.375 40.625",
        "100.0 84.375 43.75",
        "100.0 84.375 46.875",
        "100.0 84.375 50.0",
        "100.0 84.375 53.125",
        "100.0 84.375 56.25",
        "100.0 84.375 59.375",
        "100.0 84.375 62.5",
        "100.0 84.375 65.625",
        "100.0 84.375 68.75",
        "100.0 84.375 71.875",
        "100.0 84.375 75.0",
        "100.0 84.375 78.125",
        "100.0 84.375 81.25",
        "100.0 84.375 84.375",
        "100.0 84.375 87.5",
        "100.0 84.375 90.625",
        "100.0 84.375 93.75",
        "100.0 84.375 96.875",
        "100.0 84.375 100.0",
        "100.0 87.5 0.0",
        "100.0 87.5 3.125",
        "100.0 87.5 6.25",
        "100.0 87.5 9.375",
        "100.0 87.5 12.5",
        "100.0 87.5 15.625",
        "100.0 87.5 18.75",
        "100.0 87.5 21.875",
        "100.0 87.5 25.0",
        "100.0 87.5 28.125",
        "100.0 87.5 31.25",
        "100.0 87.5 34.375",
        "100.0 87.5 37.5",
        "100.0 87.5 40.625",
        "100.0 87.5 43.75",
        "100.0 87.5 46.875",
        "100.0 87.5 50.0",
        "100.0 87.5 53.125",
        "100.0 87.5 56.25",
        "100.0 87.5 59.375",
        "100.0 87.5 62.5",
        "100.0 87.5 65.625",
        "100.0 87.5 68.75",
        "100.0 87.5 71.875",
        "100.0 87.5 75.0",
        "100.0 87.5 78.125",
        "100.0 87.5 81.25",
        "100.0 87.5 84.375",
        "100.0 87.5 87.5",
        "100.0 87.5 90.625",
        "100.0 87.5 93.75",
        "100.0 87.5 96.875",
        "100.0 87.5 100.0",
        "100.0 90.625 0.0",
        "100.0 90.625 3.125",
        "100.0 90.625 6.25",
        "100.0 90.625 9.375",
        "100.0 90.625 12.5",
        "100.0 90.625 15.625",
        "100.0 90.625 18.75",
        "100.0 90.625 21.875",
        "100.0 90.625 25.0",
        "100.0 90.625 28.125",
        "100.0 90.625 31.25",
        "100.0 90.625 34.375",
        "100.0 90.625 37.5",
        "100.0 90.625 40.625",
        "100.0 90.625 43.75",
        "100.0 90.625 46.875",
        "100.0 90.625 50.0",
        "100.0 90.625 53.125",
        "100.0 90.625 56.25",
        "100.0 90.625 59.375",
        "100.0 90.625 62.5",
        "100.0 90.625 65.625",
        "100.0 90.625 68.75",
        "100.0 90.625 71.875",
        "100.0 90.625 75.0",
        "100.0 90.625 78.125",
        "100.0 90.625 81.25",
        "100.0 90.625 84.375",
        "100.0 90.625 87.5",
        "100.0 90.625 90.625",
        "100.0 90.625 93.75",
        "100.0 90.625 96.875",
        "100.0 90.625 100.0",
        "100.0 93.75 0.0",
        "100.0 93.75 3.125",
        "100.0 93.75 6.25",
        "100.0 93.75 9.375",
        "100.0 93.75 12.5",
        "100.0 93.75 15.625",
        "100.0 93.75 18.75",
        "100.0 93.75 21.875",
        "100.0 93.75 25.0",
        "100.0 93.75 28.125",
        "100.0 93.75 31.25",
        "100.0 93.75 34.375",
        "100.0 93.75 37.5",
        "100.0 93.75 40.625",
        "100.0 93.75 43.75",
        "100.0 93.75 46.875",
        "100.0 93.75 50.0",
        "100.0 93.75 53.125",
        "100.0 93.75 56.25",
        "100.0 93.75 59.375",
        "100.0 93.75 62.5",
        "100.0 93.75 65.625",
        "100.0 93.75 68.75",
        "100.0 93.75 71.875",
        "100.0 93.75 75.0",
        "100.0 93.75 78.125",
        "100.0 93.75 81.25",
        "100.0 93.75 84.375",
        "100.0 93.75 87.5",
        "100.0 93.75 90.625",
        "100.0 93.75 93.75",
        "100.0 93.75 96.875",
        "100.0 93.75 100.0",
        "100.0 96.875 0.0",
        "100.0 96.875 3.125",
        "100.0 96.875 6.25",
        "100.0 96.875 9.375",
        "100.0 96.875 12.5",
        "100.0 96.875 15.625",
        "100.0 96.875 18.75",
        "100.0 96.875 21.875",
        "100.0 96.875 25.0",
        "100.0 96.875 28.125",
        "100.0 96.875 31.25",
        "100.0 96.875 34.375",
        "100.0 96.875 37.5",
        "100.0 96.875 40.625",
        "100.0 96.875 43.75",
        "100.0 96.875 46.875",
        "100.0 96.875 50.0",
        "100.0 96.875 53.125",
        "100.0 96.875 56.25",
        "100.0 96.875 59.375",
        "100.0 96.875 62.5",
        "100.0 96.875 65.625",
        "100.0 96.875 68.75",
        "100.0 96.875 71.875",
        "100.0 96.875 75.0",
        "100.0 96.875 78.125",
        "100.0 96.875 81.25",
        "100.0 96.875 84.375",
        "100.0 96.875 87.5",
        "100.0 96.875 90.625",
        "100.0 96.875 93.75",
        "100.0 96.875 96.875",
        "100.0 96.875 100.0",
        "100.0 100.0 0.0",
        "100.0 100.0 3.125",
        "100.0 100.0 6.25",
        "100.0 100.0 9.375",
        "100.0 100.0 12.5",
        "100.0 100.0 15.625",
        "100.0 100.0 18.75",
        "100.0 100.0 21.875",
        "100.0 100.0 25.0",
        "100.0 100.0 28.125",
        "100.0 100.0 31.25",
        "100.0 100.0 34.375",
        "100.0 100.0 37.5",
        "100.0 100.0 40.625",
        "100.0 100.0 43.75",
        "100.0 100.0 46.875",
        "100.0 100.0 50.0",
        "100.0 100.0 53.125",
        "100.0 100.0 56.25",
        "100.0 100.0 59.375",
        "100.0 100.0 62.5",
        "100.0 100.0 65.625",
        "100.0 100.0 68.75",
        "100.0 100.0 71.875",
        "100.0 100.0 75.0",
        "100.0 100.0 78.125",
        "100.0 100.0 81.25",
        "100.0 100.0 84.375",
        "100.0 100.0 87.5",
        "100.0 100.0 90.625",
        "100.0 100.0 93.75",
        "100.0 100.0 96.875",
        "100.0 100.0 100.0",
    ]
