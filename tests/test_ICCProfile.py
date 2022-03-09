# -*- coding: utf-8 -*-
"""Tests for the DisplayCAL.ICCProfile module."""

from DisplayCAL import ICCProfile, colormath


def test_iccprofile_from_rgb_space():
    """Testing if the ICCProfile.from_rgb_space() method is working properly."""
    rec709_gamma18 = list(colormath.get_rgb_space("Rec. 709"))
    icc = ICCProfile.ICCProfile.from_rgb_space(rec709_gamma18, b"Rec. 709 gamma 1.8")

    assert icc is not None
    result = icc.get_info()
    assert isinstance(result, list)

    expected_result = [
        ["Size", "0 Bytes (0.00 KiB)"],
        ["Preferred CMM", "0x6172676C 'argl' ArgyllCMS"],
        ["ICC version", "2.2"],
        ["Profile class", "Display device profile"],
        ["Color model", "RGB"],
        ["Profile connection space (PCS)", "XYZ"],
        ["Created", "2022-03-09 00:19:53"],
        ["Platform", "0x2A6E6978 '*nix'"],
        ["Is embedded", "No"],
        ["Can be used independently", "Yes"],
        ["Device", ""],
        ["    Manufacturer", "0x00000000"],
        ["    Model", "0x00000000"],
        ["    Media attributes", "Reflective, Glossy, Positive, Color"],
        ["Default rendering intent", "Perceptual"],
        ["PCS illuminant XYZ", " 96.42 100.00  82.49 (xy 0.3457 0.3585, CCT 5000K)"],
        ["Creator", "0x4443414C 'DCAL' DisplayCAL"],
        ["Checksum", "0xAF709A5BE63B00419875A95394AE7EDF"],
        ["    Checksum OK", "Yes"],
        ["Description (ASCII)", "Rec. 709 gamma 1.8"],
        ["Copyright", "No copyright"],
        ["Media white point", ""],
        ["    Illuminant-relative XYZ", " 95.05 100.00 108.91 (xy 0.3127 0.3290)"],
        ["    Illuminant-relative CCT", "6503K"],
        ["        ΔE 2000 to daylight locus", "0.09"],
        ["        ΔE 2000 to blackbody locus", "4.57"],
        ["Absolute to media relative transform", "Bradford"],
        ["    Matrix", "0.8951 0.2664 -0.1614"],
        ["        ", "-0.7502 1.7135 0.0367"],
        ["        ", "0.0389 -0.0685 1.0296"],
        ["Chromaticity (illuminant-relative)", ""],
        ["    Channel 1 (b'R') xy", "0.6400 0.3300"],
        ["    Channel 2 (b'G') xy", "0.3000 0.6000"],
        ["    Channel 3 (b'B') xy", "0.1500 0.0600"],
        ["Red matrix column", ""],
        ["    Illuminant-relative XYZ", " 41.24  21.26   1.93 (xy 0.6400 0.3300)"],
        ["    PCS-relative XYZ", " 43.60  22.25   1.39 (xy 0.6484 0.3309)"],
        ["Red tone response curve", ""],
        ["    Number of entries", "1024"],
        ["    Transfer function", "Rec. 709"],
        ["    Minimum Y", "0.0000"],
        ["    Maximum Y", "100.00"],
        ["Green matrix column", ""],
        ["    Illuminant-relative XYZ", " 35.76  71.52  11.92 (xy 0.3000 0.6000)"],
        ["    PCS-relative XYZ", " 38.51  71.69   9.71 (xy 0.3212 0.5979)"],
        ["Green tone response curve", ""],
        ["    Number of entries", "1024"],
        ["    Transfer function", "Rec. 709"],
        ["    Minimum Y", "0.0000"],
        ["    Maximum Y", "100.00"],
        ["Blue matrix column", ""],
        ["    Illuminant-relative XYZ", " 18.05   7.22  95.05 (xy 0.1500 0.0600)"],
        ["    PCS-relative XYZ", " 14.30   6.06  71.39 (xy 0.1559 0.0661)"],
        ["Blue tone response curve", ""],
        ["    Number of entries", "1024"],
        ["    Transfer function", "Rec. 709"],
        ["    Minimum Y", "0.0000"],
        ["    Maximum Y", "100.00"],
    ]
    # can't set the created checksum properly
    import binascii
    from time import strftime

    expected_result[6] = [
        "Created",
        strftime("%Y-%m-%d %H:%M:%S", icc.dateTime.timetuple()),
    ]
    expected_result[17] = [
        "Checksum",
        "0x{}".format(binascii.hexlify(icc.ID).upper().decode()),
    ]

    assert result == expected_result


def test_iccprofile_from_chromaticies():
    """Testing if the ICCProfile.from_chromaticies() method is working properly."""
    xy = [
        (0.6771560743827527, 0.32205471727089957),
        (0.19945851033134956, 0.7266949701661809),
        (0.1515536624045438, 0.04081563046813107),
        (0.3133857119826585, 0.3283378912104931),
    ]
    desc = "Monitor 1 #1 2022-02-13 20-53 D6500 2.2 VF-S XYZLUT+MTX"
    copyright = "No copyright. Created with DisplayCAL 3.8.9.3 and ArgyllCMS 2.3.0"
    display_manufacturer = None
    display_name = "Monitor 1, Output DP-2"
    cat = "Bradford"

    ICCProfile.debug = True
    icc = ICCProfile.ICCProfile.from_chromaticities(
        xy[0][0],
        xy[0][1],
        xy[1][0],
        xy[1][1],
        xy[2][0],
        xy[2][1],
        xy[3][0],
        xy[3][1],
        2.2,
        desc,
        copyright,
        display_manufacturer,
        display_name,
        cat=cat,
    )

    assert isinstance(icc, ICCProfile.ICCProfile)


def test_iccprofile_get_info():
    """Testing if the ICCProfile.get_info() method is working properly."""
    xy = [
        (0.6771560743827527, 0.32205471727089957),
        (0.19945851033134956, 0.7266949701661809),
        (0.1515536624045438, 0.04081563046813107),
        (0.3133857119826585, 0.3283378912104931),
    ]
    desc = "Monitor 1 #1 2022-02-13 20-53 D6500 2.2 VF-S XYZLUT+MTX"
    copyright = "No copyright. Created with DisplayCAL 3.8.9.3 and ArgyllCMS 2.3.0"
    display_manufacturer = None
    display_name = "Monitor 1, Output DP-2"
    cat = "Bradford"

    from DisplayCAL import ICCProfile

    ICCProfile.debug = True
    icc = ICCProfile.ICCProfile.from_chromaticities(
        xy[0][0],
        xy[0][1],
        xy[1][0],
        xy[1][1],
        xy[2][0],
        xy[2][1],
        xy[3][0],
        xy[3][1],
        2.2,
        desc,
        copyright,
        display_manufacturer,
        display_name,
        cat=cat,
    )

    result = icc.get_info()
    assert isinstance(result, list)

    expected_result = [
        ["Size", "0 Bytes (0.00 KiB)"],
        ["Preferred CMM", "0x6172676C 'argl' ArgyllCMS"],
        ["ICC version", "2.2"],
        ["Profile class", "Display device profile"],
        ["Color model", "RGB"],
        ["Profile connection space (PCS)", "XYZ"],
        ["Created", "2022-02-14 02:44:22"],
        ["Platform", "0x2A6E6978 '*nix'"],
        ["Is embedded", "No"],
        ["Can be used independently", "Yes"],
        ["Device", ""],
        ["    Manufacturer", "0x00000000"],
        ["    Model", "0x00000000"],
        ["    Media attributes", "Reflective, Glossy, Positive, Color"],
        ["Default rendering intent", "Perceptual"],
        ["PCS illuminant XYZ", " 96.42 100.00  82.49 (xy 0.3457 0.3585, CCT 5000K)"],
        ["Creator", "0x4443414C 'DCAL' DisplayCAL"],
        ["Checksum", "0x02F595E98437CAF1593DB03F9DCD15C9"],
        ["    Checksum OK", "Yes"],
        ["Description", ""],
        ["    ASCII", "Monitor 1 #1 2022-02-13 20-53 D6500 2.2 VF-S XYZLUT+MTX"],
        ["    Unicode", "Monitor 1 #1 2022-02-13 20-53 D6500 2.2 VF-S XYZLUT+MTX"],
        [
            "Copyright",
            "No copyright. Created with DisplayCAL 3.8.9.3 and ArgyllCMS 2.3.0",
        ],
        ["Device model name", ""],
        ["    ASCII", "Monitor 1, Output DP-2"],
        ["    Unicode", "Monitor 1, Output DP-2"],
        ["Media white point", ""],
        ["    Illuminant-relative XYZ", " 95.45 100.00 109.12 (xy 0.3134 0.3283)"],
        ["    Illuminant-relative CCT", "6471K"],
        ["        ΔE 2000 to daylight locus", "1.18"],
        ["        ΔE 2000 to blackbody locus", "3.66"],
        ["Absolute to media relative transform", "Bradford"],
        ["    Matrix", "0.8951 0.2664 -0.1614"],
        ["        ", "-0.7502 1.7135 0.0367"],
        ["        ", "0.0389 -0.0685 1.0296"],
        ["Chromaticity (illuminant-relative)", ""],
        ["    Channel 1 (b'R') xy", "0.6772 0.3221"],
        ["    Channel 2 (b'G') xy", "0.1995 0.7267"],
        ["    Channel 3 (b'B') xy", "0.1516 0.0408"],
        ["Red matrix column", ""],
        ["    Illuminant-relative XYZ", " 57.78  27.48   0.07 (xy 0.6772 0.3221)"],
        ["    PCS-relative XYZ", " 60.96  28.84  -0.07 (xy 0.6794 0.3214)"],
        ["Red tone response curve", "Gamma 2.2"],
        ["Green matrix column", ""],
        ["    Illuminant-relative XYZ", " 18.49  67.35   6.84 (xy 0.1995 0.7267)"],
        ["    PCS-relative XYZ", " 20.41  67.24   6.00 (xy 0.2180 0.7180)"],
        ["Green tone response curve", "Gamma 2.2"],
        ["Blue matrix column", ""],
        ["    Illuminant-relative XYZ", " 19.18   5.17 102.21 (xy 0.1516 0.0408)"],
        ["    PCS-relative XYZ", " 15.05   3.92  76.56 (xy 0.1575 0.0411)"],
        ["Blue tone response curve", "Gamma 2.2"],
    ]

    # can't set the created checksum properly
    import binascii
    from time import strftime

    expected_result[6] = [
        "Created",
        strftime("%Y-%m-%d %H:%M:%S", icc.dateTime.timetuple()),
    ]
    expected_result[17] = [
        "Checksum",
        "0x{}".format(binascii.hexlify(icc.ID).upper().decode()),
    ]
    assert result == expected_result


def test_iccprofile_from_xyz():
    """Testing if ICCProfile.from_xyz() method is working properly."""
    XYZ = {
        "r": [0.5777977275512667, 0.2747999919455954, 0.0006734086960673902],
        "g": [0.18487094167718518, 0.6735475123298383, 0.06844569117319045],
        "b": [0.19179233077154842, 0.05165249572456644, 1.0220629001307424],
    }
    wXYZ = (0.9544610000000001, 1.0, 1.091182)

    desc = b"Monitor 1 #1 2022-02-13 20-53 D6500 2.2 VF-S XYZLUT+MTX"
    copyright = b"No copyright. Created with DisplayCAL 3.8.9.3 and ArgyllCMS 2.3.0"
    display_manufacturer = None
    display_name = b"Monitor 1, Output DP-2"
    cat = "Bradford"

    from DisplayCAL import ICCProfile

    ICCProfile.debug = True
    mtx = ICCProfile.ICCProfile.from_XYZ(
        XYZ["r"],
        XYZ["g"],
        XYZ["b"],
        wXYZ,
        2.2,
        desc,
        copyright,
        display_manufacturer,
        display_name,
        cat=cat,
    )

    assert isinstance(mtx, ICCProfile.ICCProfile)


def test_uInt8Number_tohex_is_working_properly():
    """Testing if uInt8Number_tohex is working properly."""
    from DisplayCAL.ICCProfile import uInt8Number_tohex

    test_value = 1321
    result = uInt8Number_tohex(test_value)
    expected_value = b")"
    assert result == expected_value


def test_uInt32Number_tohex_is_working_properly():
    """Testing if uInt32Number_tohex is working properly."""
    from DisplayCAL.ICCProfile import uInt32Number_tohex

    test_value = 132123
    result = uInt32Number_tohex(test_value)
    expected_value = b"\x00\x02\x04\x1b"
    assert result == expected_value


def test_s15Fixed16Number_tohex_is_working_properly():
    """Testing if s15Fixed16Number_tohex is working properly."""
    from DisplayCAL.ICCProfile import s15Fixed16Number_tohex

    test_value = 123.12
    result = s15Fixed16Number_tohex(test_value)
    expected_value = b"\x00{\x1e\xb8"
    assert result == expected_value


def test_uInt16Number_tohex_tohex_is_working_properly():
    """Testing if uInt16Number_tohex is working properly."""
    from DisplayCAL.ICCProfile import uInt16Number_tohex

    test_value = 12123
    result = uInt16Number_tohex(test_value)
    expected_value = b"/["
    assert result == expected_value


def test_dict_type():
    """Testing the DictType."""
    from DisplayCAL.ICCProfile import DictType

    d = DictType()
    d.update(
        {
            "CMF_product": "DisplayCAL",
            "CMF_binary": "DisplayCAL",
            "CMF_version": "3.8.9.3",
        }
    )

    expected = (
        b"dict\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x10\x00\x00\x00@"
        b"\x00\x00\x00\x16\x00\x00\x00X\x00\x00\x00\x14\x00\x00\x00l\x00\x00\x00\x14"
        b"\x00\x00\x00\x80\x00\x00\x00\x14\x00\x00\x00\x94\x00\x00\x00\x16"
        b"\x00\x00\x00\xac\x00\x00\x00\x0e\x00C\x00M\x00F\x00_\x00p\x00r\x00o\x00d"
        b"\x00u\x00c\x00t\x00\x00\x00D\x00i\x00s\x00p\x00l\x00a\x00y\x00C\x00A\x00L"
        b"\x00C\x00M\x00F\x00_\x00b\x00i\x00n\x00a\x00r\x00y\x00D\x00i\x00s\x00p"
        b"\x00l\x00a\x00y\x00C\x00A\x00L\x00C\x00M\x00F\x00_\x00v\x00e\x00r\x00s"
        b"\x00i\x00o\x00n\x00\x00\x003\x00.\x008\x00.\x009\x00.\x003\x00\x00"
    )

    assert d.tagData == expected


def test_sample_icc_file_1(data_files):
    """Test with sample icc files.

    Args:
        data_files: A fixture supplying data files.
    """
    from DisplayCAL import ICCProfile

    icc_profile = ICCProfile.ICCProfile(profile=data_files["default.icc"].absolute())
    result = icc_profile.get_info()

    expected_result = [
        ["Size", "20240 Bytes (19.77 KiB)"],
        ["Preferred CMM", "0x6172676C 'argl' ArgyllCMS"],
        ["ICC version", "2.2"],
        ["Profile class", "Display device profile"],
        ["Color model", "RGB"],
        ["Profile connection space (PCS)", "XYZ"],
        ["Created", "2016-01-08 00:59:09"],
        ["Platform", "Microsoft"],
        ["Is embedded", "No"],
        ["Can be used independently", "Yes"],
        ["Device", ""],
        ["    Manufacturer", "0x00000000"],
        ["    Model", "0x00000000"],
        ["    Media attributes", "Reflective, Glossy, Positive, Color"],
        ["Default rendering intent", "Media-relative colorimetric"],
        ["PCS illuminant XYZ", " 96.42 100.00  82.49 (xy 0.3457 0.3585, CCT 5000K)"],
        ["Creator", "0x6172676C 'argl' ArgyllCMS"],
        ["Checksum", "0xCE27ED7FC7C06FBB9492BC1408729D6C"],
        ["    Checksum OK", "Yes"],
        ["Description (ASCII)", "DisplayCAL calibration preset: Default"],
        ["Copyright", "Created with DisplayCAL and Argyll CMS"],
        ["Media white point", ""],
        ["    Illuminant-relative XYZ", " 95.05 100.00 108.91 (xy 0.3127 0.3290)"],
        ["    Illuminant-relative CCT", "6503K"],
        ["        ΔE 2000 to daylight locus", "0.09"],
        ["        ΔE 2000 to blackbody locus", "4.57"],
        ["Media black point", ""],
        ["    Illuminant-relative XYZ", "0.0000 0.0000 0.0000"],
        ["Video card gamma table", ""],
        ["    Bitdepth", "16"],
        ["    Channels", "3"],
        ["    Number of entries per channel", "256"],
        ["    Channel 1 gamma at 50% input", "1.00"],
        ["    Channel 1 minimum", "0.0000%"],
        ["    Channel 1 maximum", "100.00%"],
        ["    Channel 1 unique values", "256 @ 8 Bit"],
        ["    Channel 1 is linear", "Yes"],
        ["    Channel 2 gamma at 50% input", "1.00"],
        ["    Channel 2 minimum", "0.0000%"],
        ["    Channel 2 maximum", "100.00%"],
        ["    Channel 2 unique values", "256 @ 8 Bit"],
        ["    Channel 2 is linear", "Yes"],
        ["    Channel 3 gamma at 50% input", "1.00"],
        ["    Channel 3 minimum", "0.0000%"],
        ["    Channel 3 maximum", "100.00%"],
        ["    Channel 3 unique values", "256 @ 8 Bit"],
        ["    Channel 3 is linear", "Yes"],
        ["Red matrix column", ""],
        ["    Illuminant-relative XYZ", " 41.24  21.26   1.93 (xy 0.6400 0.3300)"],
        ["    PCS-relative XYZ", " 43.60  22.25   1.39 (xy 0.6484 0.3309)"],
        ["Green matrix column", ""],
        ["    Illuminant-relative XYZ", " 35.76  71.52  11.92 (xy 0.3000 0.6000)"],
        ["    PCS-relative XYZ", " 38.51  71.69   9.71 (xy 0.3212 0.5979)"],
        ["Blue matrix column", ""],
        ["    Illuminant-relative XYZ", " 18.05   7.22  95.05 (xy 0.1500 0.0600)"],
        ["    PCS-relative XYZ", " 14.31   6.06  71.39 (xy 0.1559 0.0661)"],
        ["Red tone response curve", ""],
        ["    Number of entries", "256"],
        ["    Transfer function", "Gamma 2.20 100%"],
        ["    Minimum Y", "0.0000"],
        ["    Maximum Y", "100.00"],
        ["Green tone response curve", ""],
        ["    Number of entries", "256"],
        ["    Transfer function", "Gamma 2.20 100%"],
        ["    Minimum Y", "0.0000"],
        ["    Maximum Y", "100.00"],
        ["Blue tone response curve", ""],
        ["    Number of entries", "256"],
        ["    Transfer function", "Gamma 2.20 100%"],
        ["    Minimum Y", "0.0000"],
        ["    Maximum Y", "100.00"],
        ["Characterization target", "[17538 Bytes]"],
        ["Absolute to media relative transform", "Bradford"],
        ["    Matrix", "0.8951 0.2664 -0.1614"],
        ["        ", "-0.7502 1.7135 0.0367"],
        ["        ", "0.0389 -0.0685 1.0296"],
    ]
    assert result == expected_result


def test_hexrepr_is_with_mapping_supplied():
    """Testing DisplayCAL.ICCProfile.hexrepr with a mapping is supplied."""
    from DisplayCAL.ICCProfile import hexrepr, cmms

    test_bytes_string = b"ADBE"
    expected_result = "0x41444245 'ADBE' Adobe"
    result = hexrepr(test_bytes_string, mapping=cmms)
    assert result == expected_result


def test_hexrepr_is_without_mapping_supplied():
    """Testing DisplayCAL.ICCProfile.hexrepr with no mapping is supplied."""
    from DisplayCAL.ICCProfile import hexrepr

    test_bytes_string = b"ADBE"
    expected_result = "0x41444245 'ADBE'"
    result = hexrepr(test_bytes_string)
    assert result == expected_result


def test_date_time_number_is_working_properly():
    """Testing if DisplayCAL.ICCProfile.dataTimeNumber function is working properly."""
    import datetime
    from DisplayCAL.ICCProfile import dateTimeNumber

    test_value = b"\x07\xe6\x00\x02\x00\x13\x00\x12\x00*\x002"
    expected_result = datetime.datetime(2022, 2, 19, 18, 42, 50)
    result = dateTimeNumber(test_value)
    assert result == expected_result


def test_icc_profile_tag_is_working_properly():
    """Testing if the ``ICCProfileTag`` class is working properly."""
    from DisplayCAL.ICCProfile import ICCProfileTag

    tag_data = b"\0\0\0\0"
    tag_signature = "desc"
    tag = ICCProfileTag(tag_data, tag_signature)
    assert tag is not None
    assert tag.tagData == tag_data
    assert tag.tagSignature == tag_signature


def test_text_tag_is_working_properly():
    """Testing if the ``Text`` Tag is working properly."""
    from DisplayCAL.ICCProfile import Text

    test_data = b"some text"
    t = Text(test_data)
    t.tagData = test_data
    t.tagSignature = "targ"

    assert str(t) == test_data.decode("UTF-8", "replace")
