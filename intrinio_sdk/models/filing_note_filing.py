# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FilingNoteFiling(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cik': 'str',
        'report_type': 'str',
        'period_end_date': 'date',
        'filing_date': 'date'
    }

    attribute_map = {
        'cik': 'cik',
        'report_type': 'report_type',
        'period_end_date': 'period_end_date',
        'filing_date': 'filing_date'
    }

    def __init__(self, cik=None, report_type=None, period_end_date=None, filing_date=None):  # noqa: E501
        """FilingNoteFiling - a model defined in Swagger"""  # noqa: E501

        self._cik = None
        self._report_type = None
        self._period_end_date = None
        self._filing_date = None
        self.discriminator = None

        if cik is not None:
            self.cik = cik
        if report_type is not None:
            self.report_type = report_type
        if period_end_date is not None:
            self.period_end_date = period_end_date
        if filing_date is not None:
            self.filing_date = filing_date

    @property
    def cik(self):
        """Gets the cik of this FilingNoteFiling.  # noqa: E501

        The Central Index Key (CIK) assigned to the company  # noqa: E501

        :return: The cik of this FilingNoteFiling.  # noqa: E501
        :rtype: str
        """
        return self._cik

    @cik.setter
    def cik(self, cik):
        """Sets the cik of this FilingNoteFiling.

        The Central Index Key (CIK) assigned to the company  # noqa: E501

        :param cik: The cik of this FilingNoteFiling.  # noqa: E501
        :type: str
        """

        self._cik = cik

    @property
    def report_type(self):
        """Gets the report_type of this FilingNoteFiling.  # noqa: E501

        The type of report (10-Q, 10-K, etc) filed  # noqa: E501

        :return: The report_type of this FilingNoteFiling.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this FilingNoteFiling.

        The type of report (10-Q, 10-K, etc) filed  # noqa: E501

        :param report_type: The report_type of this FilingNoteFiling.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def period_end_date(self):
        """Gets the period_end_date of this FilingNoteFiling.  # noqa: E501

        The ending date of the fiscal period for the filing  # noqa: E501

        :return: The period_end_date of this FilingNoteFiling.  # noqa: E501
        :rtype: date
        """
        return self._period_end_date

    @period_end_date.setter
    def period_end_date(self, period_end_date):
        """Sets the period_end_date of this FilingNoteFiling.

        The ending date of the fiscal period for the filing  # noqa: E501

        :param period_end_date: The period_end_date of this FilingNoteFiling.  # noqa: E501
        :type: date
        """

        self._period_end_date = period_end_date

    @property
    def filing_date(self):
        """Gets the filing_date of this FilingNoteFiling.  # noqa: E501

        The date the report was filed with the SEC  # noqa: E501

        :return: The filing_date of this FilingNoteFiling.  # noqa: E501
        :rtype: date
        """
        return self._filing_date

    @filing_date.setter
    def filing_date(self, filing_date):
        """Sets the filing_date of this FilingNoteFiling.

        The date the report was filed with the SEC  # noqa: E501

        :param filing_date: The filing_date of this FilingNoteFiling.  # noqa: E501
        :type: date
        """

        self._filing_date = filing_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FilingNoteFiling):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other