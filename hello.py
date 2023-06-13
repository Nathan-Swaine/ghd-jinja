from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <div role="article" aria-roledescription="email" aria-label="" lang="en">
    <table style="font-family: Helvetica, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif; width: 100%;" cellpadding="0" cellspacing="0" role="presentation">
        <tr>
            <td align="center" style="background: #000000;">
                <table class="sm-w-full" style="width: 800px; background: #000000;" cellpadding="0" cellspacing="0" role="presentation">
                    <tr>
                        <td align="center" valign="top">
                            <table cellpadding="0" cellspacing="0" border="0" width="100%" align="center" bgcolor="#000000">
                                <!--[if !mso]><!-- -->
                                <tr>
                                    <td height="40" align="center" valign="middle">
                                        <table cellpadding="0" cellspacing="0" border="0" width="100%" bgcolor="#000000"><?php
                                            if (isset($preheader)) {
                                                ?>
                                                    <tr>
                                                        <td width="0" height="0" align="center" style="display:none !important;visibility:hidden;mso-hide:all;font-size:1px;color:#000000;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;">
                                                            <?php
                                                                echo $preheader . "&nbsp;" . "&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;";
                                                            ?>
                                                        </td>
                                                    </tr>
                                                <?php
                                                }
                                            ?>
                                            </table>
                                        </td>
                                </tr>
                                    <!--<![endif]-->
                                <tr>
                                    <td align="center" valign="middle">
                                        <table border="0" cellpadding="0" width="100%" cellspacing="0"  bgcolor="#000000" style="padding-bottom: 30px;">
                                            <tr>
                                                <td align="center" valign="middle">
                                                    <table border="0" cellpadding="0" width="100%" cellspacing="0"  bgcolor="#000000">
                                                        <tr>
                                                            <td align="right" class="paragraph fine-print" style="color: #999 !important; -webkit-font-smoothing: antialiased;-moz-font-smoothing: antialiased;-o-font-smoothing: antialiased; font-size: 13px !important; line-height: 18px !important; padding-right: 25px;">
                                                                Can't read this email? <a href="&&&" title="View email online"><b style="-webkit-font-smoothing: antialiased;-moz-font-smoothing: antialiased;-o-font-smoothing: antialiased; font-size: 13px !important; line-height: 18px !important; color:#999; text-decoration: underline;">View it online</b>
                                                            </a>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <td valign="top" align="center">
                            <table class="sm-w-full" style="width: 800px; background: #000000;" cellpadding="0" cellspacing="0" role="presentation">
                                <tr>
                                    <td class="" width="80%" align="center" style="padding-bottom: 30px;">
                                        <img src="http://26ffb5095c072cf03267-e6198fb5b35e7ff13409c8fbe7eef8a1.r85.cf3.rackcdn.com/core/header-2021/header-logo.jpg" width="25%" style="max-width: 120px!important;" alt="">
                                    </td>
                                </tr>
                                <tr>
                                    <td valign="top" align="center" width="100%" style="padding-bottom:10px;" >
                                        <table style="width: auto; background: #000000;" cellpadding="0" cellspacing="0" role="presentation" style="color: #ffffff; font-family: Helvetica, Arial, sans-serif; text-align: center;">
                                            <tr>
                                                <td class="header-buttons" valign="top" align="center" style="color: #ffffff; font-size: 14px; font-family: Helvetica, Arial, sans-serif; font-weight: bold; padding-right: 15px;">
                                                    <a href="https://www.ghdhair.com/hair-straighteners-c" style="text-decoration: none; color: #ffffff; font-weight: bold;">
                                                        <font color="#ffffff" style="color: #ffffff !important; text-decoration: none !important;">
                                                            <strong style="font-weight: bold; text-decoration: none;">HAIR STRAIGHTENERS</strong>
                                                        </font>
                                                    </a>
                                                </td>
                                                <td class="header-buttons" valign="top" align="center" style="color: #ffffff; font-size: 14px; font-family: Helvetica, Arial, sans-serif; font-weight: bold; padding-right: 15px;">
                                                    <a href="https://www.ghdhair.com/hot-air-stylers-c" style="text-decoration: none; color: #ffffff; font-weight: bold;">
                                                        <font color="#ffffff" style="color: #ffffff !important; text-decoration: none !important;">
                                                            <strong style="font-weight: bold; text-decoration: none;">HOT AIR STYLERS</strong>
                                                        </font>
                                                    </a>
                                                </td>
                                                <td class="header-buttons" valign="top" align="center" style="color: #ffffff; font-size: 14px; font-family: Helvetica, Arial, sans-serif; font-weight: bold; padding-right: 15px;">
                                                    <a href="https://www.ghdhair.com/curling-wands-and-tongs-c" style="text-decoration: none; color: #ffffff; font-weight: bold;">
                                                    <font color="#ffffff" style="color: #ffffff !important; text-decoration: none !important;">
                                                            <strong style="font-weight: bold; text-decoration: none;">HAIR CURLERS</strong>
                                                        </font>
                                                    </a>
                                                </td>
                                                <td class="header-buttons-last" valign="top" align="center" style="color: #ffffff; font-size: 14px; font-family: Helvetica, Arial, sans-serif; font-weight: bold; padding-right: 15px;">
                                                    <a href="https://www.ghdhair.com/hair-dryers-c" style="text-decoration: none; color: #ffffff; font-weight: bold;">
                                                        <font color="#ffffff" style="color: #ffffff !important; text-decoration: none !important;">
                                                            <strong style="font-weight: bold; text-decoration: none;">HAIR DRYERS</strong>
                                                        </font>
                                                    </a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <table style="font-family: Helvetica, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', sans-serif; width: 100%;" cellpadding="0" align="center" bgcolor="#000000"cellspacing="0" role="presentation">
        <tr>
            <td valign="top" align="center">
        <table class="sm-w-full" cellpadding="0" cellspacing="0" role="presentation" style="width: 800px; background: #000000;">
            <tr>
                <td cellpadding="0" width="100%" cellspacing="0" dir="ltr" valign="top" align="center" bgcolor="#000000" class=" sm-w-full inline-block  pb-20 " style="background-color: #000000; padding-bottom:30px; ">
                    <a href="https://www.ghdhair.com/curling-wands-and-tongs-c"> <img src="http://c94df97feba3ed270b40-dccdaa2c75856b59b01c3723d5ef3b50.r0.cf3.rackcdn.com/promo_2023/15-curve/uk-1.jpg" alt="" valign="top" width="800" height="518" border="0" class="always-full-width" style="width:100%;height:auto;min-width:auto;display: block; min-width: 800px; width: 800px;"></a>
                </td>
            </tr>
            <tr style="background: #000000;">
                <td align="center" class="" style=" padding-bottom: 50px;">
                    <a href="https://www.ghdhair.com/curling-wands-and-tongs-c"><img src="http://c94df97feba3ed270b40-dccdaa2c75856b59b01c3723d5ef3b50.r0.cf3.rackcdn.com/promo_2023/15-curve/uk-2.jpg" alt="" valign="top" width="800" height="165" border="0" class="always-full-width" style="width:100%;height:auto;min-width:auto;display: block; min-width: 800px; width: 800px;"></a>
                </td>
            </tr>
            <tr>
                <td valign="top" align="center" style="background: #000000;">
                    <table width="90%" align="center" cellpadding="0" cellspacing="0" role="presentation">
                        <tr>
                            <th valign="top" bgcolor="#000000" class=" body-text px-3  " align="center" style="
                                font-family: Helvetica, Arial, sans-serif;
                                font-size: 18px;
                                font-weight: lighter;
                                text-align: center;
                                line-height: 19px !important;
                                letter-spacing: 0px;
                                color: #ffffff;
                                padding-left: 30px;
                                padding-right: 30px;
                                padding-bottom: 30px;">
                                From hair tongs to stylers and hair dryers, we&rsquo;ve got the styling tool to achieve your desired look. Hurry! Take 15% off* for a limited time only on selected styling heated tools. <br><br><span style=" font-weight: 700; font-size: 20px;">USE CODE: <span style="color: #d6af63;">GHD 15</span></span>
                            </th>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td align="center" valign="top" bgcolor="#000000" style="border-collapse:collapse;padding:0;margin:0; ">
                    <table valign="center" align="center" bgcolor="#000000" cellpadding="0" cellspacing="0">
                        <tr>
                            <td class="pr-30 pl-30  cta-float-none  pl-0 pr-0 " cellpadding="0" cellspacing="0" border="0" valign="bottom" align="center" bgcolor="#000000" style="background-color: #000000; padding-left: 25px; padding-right: 25px; text-align: center; font-weight: bold; padding-bottom: 100px;">
                                <table valign="center" align="center" bgcolor="#000000" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td align="center" width="200" strokecolor="000000" style="
                                                width:200;
                                                padding-top:10px;
                                                padding-bottom:10px;
                                                padding-left:10px;
                                                padding-right:10px;
                                                font-family: Helvetica, Arial, sans-serif;
                                                font-size:16px;
                                                line-height: 25px !important;
                                                vertical-align: middle;
                                                background-color: #f8f8f8;
                                                text-align: center;">
                                                    <a strokecolor="#000000" href="https://www.ghdhair.com/curling-wands-and-tongs-c" style="
                                                        display: inline-block;
                                                        color: #000000 !important; 
                                                        background-color: #f8f8f8;
                                                        text-decoration: none;
                                                        font-size: 16px;
                                                        font-weight: bolder;
                                                        border-color: #ffffff;">
                                                        <font style="color: rgb(0,0,0);">
                                                            SHOP NOW                                                </font>
                                                    </a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td cellpadding="0" width="100%" cellspacing="0" dir="ltr" valign="top" align="center" bgcolor="#000000" class=" sm-w-full inline-block  pb-20 " style="background-color: #000000; padding-bottom:30px; ">
                    <a href="https://www.ghdhair.com/personalise-c"> <img src="http://c94df97feba3ed270b40-dccdaa2c75856b59b01c3723d5ef3b50.r0.cf3.rackcdn.com/promo_2023/15-curve/uk-3.jpg" alt="" valign="top" width="800" height="513" border="0" class="always-full-width" style="width:100%;height:auto;min-width:auto;display: block; min-width: 800px; width: 800px;"></a>
                </td>
            </tr>
            <tr style="background: #000000;">
                <td align="center" class="" style=" padding-bottom: 50px;">
                    <a href="https://www.ghdhair.com/personalise-c"><img src="http://c94df97feba3ed270b40-dccdaa2c75856b59b01c3723d5ef3b50.r0.cf3.rackcdn.com/promo_2023/15-curve/uk-4.jpg" alt="" valign="top" width="800" height="78" border="0" class="always-full-width" style="width:100%;height:auto;min-width:auto;display: block; min-width: 800px; width: 800px;"></a>
                </td>
            </tr>
            <tr>
                <td valign="top" align="center" style="background: #000000;">
                    <table width="90%" align="center" cellpadding="0" cellspacing="0" role="presentation">
                        <tr>
                            <th valign="top" bgcolor="#000000" class=" body-text px-3  " align="center" style="
                                font-family: Helvetica, Arial, sans-serif;
                                font-size: 18px;
                                font-weight: lighter;
                                text-align: center;
                                line-height: 19px !important;
                                letter-spacing: 0px;
                                color: #ffffff;
                                padding-left: 30px;
                                padding-right: 30px;
                                padding-bottom: 30px;">
                                Your hair is unique, so why not make your mark by personalising your new tool? Engrave your name or words that mean something to you on a variety of selected heated styling tools**! The perfect gift for yourself or your loved ones.
                            </th>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td align="center" valign="top" bgcolor="#000000" style="border-collapse:collapse;padding:0;margin:0; ">
                    <table valign="center" align="center" bgcolor="#000000" cellpadding="0" cellspacing="0">
                        <tr>
                            <td class="pr-30 pl-30  cta-float-none  pl-0 pr-0 " cellpadding="0" cellspacing="0" border="0" valign="bottom" align="center" bgcolor="#000000" style="background-color: #000000; padding-left: 25px; padding-right: 25px; text-align: center; font-weight: bold; padding-bottom: 100px;">
                                <table valign="center" align="center" bgcolor="#000000" cellpadding="0" cellspacing="0">
                                    <tr>
                                        <td align="center" width="200" strokecolor="000000" style="
                                            width:200;
                                            padding-top:10px;
                                            padding-bottom:10px;
                                            padding-left:10px;
                                            padding-right:10px;
                                            font-family: Helvetica, Arial, sans-serif;
                                            font-size:16px;
                                            line-height: 25px !important;
                                            vertical-align: middle;
                                            background-color: #f8f8f8;
                                            text-align: center;">
                                                <a strokecolor="#000000" href="https://www.ghdhair.com/personalise-c" style="
                                                    display: inline-block;
                                                    color: #000000 !important; 
                                                    background-color: #f8f8f8;
                                                    text-decoration: none;
                                                    font-size: 16px;
                                                    font-weight: bolder;
                                                    border-color: #ffffff;">
                                                    <font style="color: rgb(0,0,0);">
                                                        SHOP NOW                                                </font>
                                                </a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>


        <tr>
            <td align="center" style="background-color: #000000; padding-top: 0; padding-bottom: 0;">
                <table class="sm-w-full" style="width: 800px; background: #000000; text-align: center; color: #d3d0d0;" cellpadding="0" cellspacing="0" role="presentation">
                    <tr>
                        <td valign="top" align="center">
                            <table width="90%" align="center" style="background: #000000;" cellpadding="0" cellspacing="0" role="presentation">
                                <tr>
                                    <td class="paragraph fine-print" align="center"  style="padding-top: 20px; padding-bottom: 20px; -webkit-font-smoothing: antialiased;-moz-font-smoothing: antialiased;-o-font-smoothing: antialiased; font-size: 13px !important; line-height: 18px !important;">
                                        <a href="http://link.ghdhair.com/u/register.php?CID=285063194&f=5754&p=2&a=r&SID=&el=&llid=&counted=&c=&inp_3=$pers_3$&endlink=https://www.ghdhair.com/unsubscribe" style="color:#fff; padding-bottom: 20px;">Click here to Unsubscribe</a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</div>
"""