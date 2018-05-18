#!/usr/bin/env python
import ec2
import redshift
import elasticsearch
import apigateway

from utils import jprint


def main():
    jprint(ec2.get_info())
    jprint(redshift.get_info())
    jprint(elasticsearch.get_info())
    jprint(apigateway.get_info())


if __name__ == '__main__':
    main()
