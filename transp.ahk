; Shift + Control + 1 - Transparency OFF
; Shift + Control + 2 - some transparency
; ...
; Shift + Control + 5 - almost max transparency

+^1::WinSetTransparent "Off", "A" ; same as "255"
+^2::WinSetTransparent 225, "A"
+^3::WinSetTransparent 200, "A"
+^4::WinSetTransparent 150, "A"
+^5::WinSetTransparent 100, "A"
+^6::WinSetTransparent 50, "A"
+^7::WinSetTransparent 40, "A"
+^8::WinSetTransparent 30, "A"
+^9::WinSetTransparent 20, "A"
+^0::WinSetTransparent 10, "A"
