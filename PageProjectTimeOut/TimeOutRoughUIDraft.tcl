#############################################################################
# Generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#  Mar 18, 2020 07:01:23 PM IST  platform: Windows NT
set vTcl(timestamp) ""


set image_list { \
    play_lightblue_png "../Users/91809/PycharmProjects/TimeoutApplication/icons/play-lightblue.png" \
    plus_green_png "../Users/91809/PycharmProjects/TimeoutApplication/icons/plus-green.png" \
    recycle_bin_png "../Users/91809/PycharmProjects/TimeoutApplication/icons/recycle-bin.png" \
    shuffle_png "../Users/91809/PycharmProjects/TimeoutApplication/icons/shuffle.png" \
    stop_lightblue_png "../Users/91809/PycharmProjects/TimeoutApplication/icons/stop-lightBlue.png" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top43 {base} {
    global vTcl
    if {$base == ""} {
        set base .top43
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m49" -background #fd4267 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1304x745+54+-11
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::separator $top.tSe45
    vTcl:DefineAlias "$top.tSe45" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
    ttk::entry $top.tEn46 \
        -font TkTextFont -foreground {} -background {} -takefocus {} \
        -cursor ibeam 
    vTcl:DefineAlias "$top.tEn46" "TEntry1" vTcl:WidgetProc "Toplevel1" 1
    bind $top.tEn46 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Enter URL here}
    }
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fd4267 -borderwidth 0 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image plus_green_png -pady 0 -text Upload 
    vTcl:DefineAlias "$top.but47" "UploadButton" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but47 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Upload Url}
    }
    label $top.lab48 \
        -activebackground #f9f9f9 -activeforeground black -background #fd4267 \
        -compound center -disabledforeground #a3a3a3 \
        -font {-family {Segoe Script} -size 16 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -justify left -text {Welcome Username} 
    vTcl:DefineAlias "$top.lab48" "Label1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m49
    menu $site_3_0 \
        -activebackground SystemHighlight \
        -activeforeground SystemHighlightText \
        -background $vTcl(pr,menubgcolor) -font TkDefaultFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    button $top.but50 \
        -activebackground #fd4267 -activeforeground #000000 \
        -background #fd4267 -borderwidth 0 -command stop -compound center \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image stop_lightblue_png -overrelief sunken -pady 0 -text Stop 
    vTcl:DefineAlias "$top.but50" "stopButton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Button 
    vTcl:DefineAlias "$top.but51" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but52 \
        -activebackground #f9f9f9 -activeforeground #000000 \
        -background #fd4267 -borderwidth 0 -command start \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image play_lightblue_png -overrelief sunken -pady 0 -text Start 
    vTcl:DefineAlias "$top.but52" "startButton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fd4267 -borderwidth 0 -command Shuffle \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightbackground #fefbb4 \
        -highlightcolor black -image shuffle_png -pady 0 -text Shuffle 
    vTcl:DefineAlias "$top.but57" "shuffleButton" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr68 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.scr68" "Scrolledlistbox2" vTcl:WidgetProc "Toplevel1" 1

    $top.scr68.01 configure -background white \
        -cursor xterm \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    label $top.lab69 \
        -activebackground #f9f9f9 -activeforeground black -background #fd4267 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe Script} -size 16 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Playlist 
    vTcl:DefineAlias "$top.lab69" "Label3" vTcl:WidgetProc "Toplevel1" 1
    spinbox $top.spi70 \
        -activebackground #f9f9f9 -background white -buttonbackground #d9d9d9 \
        -disabledforeground #a3a3a3 -font TkDefaultFont -foreground black \
        -from 1.0 -highlightbackground black -highlightcolor black \
        -increment 1.0 -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable spinbox -to 100.0 -values 20 
    vTcl:DefineAlias "$top.spi70" "Spinbox1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab71 \
        -activebackground #f9f9f9 -activeforeground black -background #fd4267 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Interval (min)} 
    vTcl:DefineAlias "$top.lab71" "Label4" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr45 \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.scr45" "Scrolledlistbox1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr45.01 configure -background white \
        -cursor xterm \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fd4267 -borderwidth 0 -command deletePlaylistElements \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image recycle_bin_png -pady 0 -text Delete 
    vTcl:DefineAlias "$top.but46" "DeleteButton" vTcl:WidgetProc "Toplevel1" 1
    bind $top.but46 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Deletes the selected elements of playlist}
    }
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab47" "TimerLabel" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab44 \
        -activebackground #f9f9f9 -activeforeground black -background #fd4267 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe Script} -size 16 -weight bold} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {User History} 
    vTcl:DefineAlias "$top.lab44" "HistoryLabel" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tSe45 \
        -in $top -x 0 -relx 0.007 -y 0 -rely 0.094 -width 0 -relwidth 0.989 \
        -height 0 -relheight 0.003 -anchor nw -bordermode inside 
    place $top.tEn46 \
        -in $top -x 0 -relx 0.046 -y 0 -rely 0.121 -width 556 -relwidth 0 \
        -height 31 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.475 -y 0 -rely 0.121 -width 40 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.015 -y 0 -rely 0.027 -width 0 -relwidth 0.209 \
        -height 0 -relheight 0.055 -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 0 -relx 0.038 -y 0 -rely 0.336 -width 0 -relwidth 0.046 \
        -height 0 -relheight 0.081 -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 0 -relx -0.107 -y 0 -rely 0.537 -height 0 \
        -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 0 -relx 0.038 -y 0 -rely 0.215 -width 0 -relwidth 0.046 \
        -height 0 -relheight 0.081 -anchor nw -bordermode ignore 
    place $top.but57 \
        -in $top -x 0 -relx 0.038 -y 0 -rely 0.443 -width 0 -relwidth 0.049 \
        -height 0 -relheight 0.081 -anchor nw -bordermode ignore 
    place $top.scr68 \
        -in $top -x 0 -y 0 -rely 0.644 -width 0 -relwidth 0.553 -height 0 \
        -relheight 0.342 -anchor nw -bordermode ignore 
    place $top.lab69 \
        -in $top -x 0 -relx 0.698 -y 0 -rely 0.215 -width 0 -relwidth 0.141 \
        -height 0 -relheight 0.028 -anchor nw -bordermode ignore 
    place $top.spi70 \
        -in $top -x 0 -relx 0.859 -y 0 -rely 0.121 -width 0 -relwidth 0.065 \
        -height 0 -relheight 0.027 -anchor nw -bordermode ignore 
    place $top.lab71 \
        -in $top -x 0 -relx 0.782 -y 0 -rely 0.121 -width 0 -relwidth 0.072 \
        -height 0 -relheight 0.028 -anchor nw -bordermode ignore 
    place $top.scr45 \
        -in $top -x 0 -relx 0.552 -y 0 -rely 0.255 -width 0 -relwidth 0.446 \
        -height 0 -relheight 0.733 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 0 -relx 0.552 -y 0 -rely 0.188 -width 97 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.176 -y 0 -rely 0.309 -width 0 -relwidth 0.238 \
        -height 0 -relheight 0.095 -anchor nw -bordermode ignore 
    place $top.lab44 \
        -in $top -x 0 -relx 0.008 -y 0 -rely 0.604 -width 0 -relwidth 0.087 \
        -height 0 -relheight 0.028 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top43 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

