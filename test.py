# -*- coding: utf-8 -*-
import oseti

analyzer = oseti.Analyzer()

while True:
    message = input( "入力: " );
    print( analyzer.analyze_detail( message ) )
