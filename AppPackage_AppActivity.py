
adb_shell_command = "adb shell"

appPackage_AppActivity = "dumpsys window windows | grep -E 'mTopActivityComponent'"


"""

snapshot=TaskSnapshot{ mId=1715834319782 mTopActivityComponent=com.google.android.apps.messaging/.main.MainActivity
mSnapshot=android.hardware.HardwareBuffer@53b1501 (864x1920) mColorSpace=sRGB IEC61966-2.1 (id=0, model=RGB)
mOrientation=1 mRotation=0 mTaskSize=Point(1080, 2400) mContentInsets=[0,63][0,126] mIsLowResolution=false
mIsRealSnapshot=true mWindowingMode=1 mAppearance=24 mIsTranslucent=false mHasImeSurface=false

snapshot=TaskSnapshot{ mId=1715836819495 mTopActivityComponent=com.android.dialer/.main.impl.MainActivity
mSnapshot=android.hardware.HardwareBuffer@f4ab887 (864x1920) mColorSpace=sRGB IEC61966-2.1 (id=0, model=RGB) 
mOrientation=1 mRotation=0 mTaskSize=Point(1080, 2400) mContentInsets=[0,63][0,126] mIsLowResolution=false
mIsRealSnapshot=true mWindowingMode=1 mAppearance=16 mIsTranslucent=false mHasImeSurface=false

snapshot=TaskSnapshot{ mId=1715846184229 mTopActivityComponent=com.android.contacts/.activities.PeopleActivity
mSnapshot=android.hardware.HardwareBuffer@8c58728 (864x1920) mColorSpace=sRGB IEC61966-2.1 (id=0, model=RGB)
mOrientation=1 mRotation=0 mTaskSize=Point(1080, 2400) mContentInsets=[0,63][0,126] mIsLowResolution=false mIsRealSnapshot=true 
mWindowingMode=1 mAppearance=0 mIsTranslucent=false mHasImeSurface=false

"""


