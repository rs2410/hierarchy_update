"""Описывает дополнительный функционал."""

import typing
import json
import csv

import exceptions


class FormatStreamTransform:

    @staticmethod
    def json_to_csv(out_stream: typing.TextIO, in_stream: typing.TextIO) -> None:
        """Преобразует json из потока out_stream в csv в поток in_stream."""

        js_str = out_stream.read()
        js = json.loads(js_str)
        if not isinstance(js, list):
            raise exceptions.JsonIsNotList
        if len(js) == 0:
            raise exceptions.JsonIsEmpty

        fieldnames = js[0].keys()

        writer = csv.DictWriter(in_stream, fieldnames, restval='null')
        # writer.writeheader()
        writer.writerows(js)


class FormatFileTransform:

    @staticmethod
    def json_to_csv(out_filename: str, in_filename: str) -> None:
        with open(out_filename, 'r') as out_file_stream,\
                open(in_filename, 'w') as in_file_stream:
            FormatStreamTransform.json_to_csv(out_file_stream, in_file_stream)


if __name__ == '__main__':
    FormatFileTransform.json_to_csv('test_data.json', 'test.csv')
