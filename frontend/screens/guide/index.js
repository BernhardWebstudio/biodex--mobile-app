import React, { useEffect } from 'react';
import { View, StyleSheet, Dimensions } from 'react-native';
import { ScreenOrientation } from 'expo';

import SwiperFlatList from '../../components/SwiperFlatList';
import HomeScreen from './HomeScreen';
import ImageCaptureScreen from './ImageCaptureScreen';
import CroppingScreen from './CroppingScreen';
import ButterflySelectionScreen from './ButterflySelectionScreen';
import StartScreen from './StartScreen';
import Theme from '../../theme';

const Guide = ({ navigation }) => {
  ScreenOrientation.lockAsync(ScreenOrientation.OrientationLock.PORTRAIT_UP);

  // Cleanup function on navigation
  useEffect(() => {
    const cleanup = navigation.addListener('blur', () => ScreenOrientation.unlockAsync());
    return cleanup;
  }, [navigation]);

  // Adding navigation focus listener and cleanup function on unmount
  useEffect(() => {
    navigation.addListener('focus', () => ScreenOrientation.lockAsync(ScreenOrientation.OrientationLock.PORTRAIT_UP));
    const cleanup = () => ScreenOrientation.unlockAsync();
    return cleanup;
  }, []);

  return (
    <View style={styles.container}>
      <SwiperFlatList index={0} showPagination navigation={navigation}>
        <HomeScreen style={styles.child} />
        <ImageCaptureScreen style={styles.child} />
        <CroppingScreen style={styles.child} />
        <ButterflySelectionScreen style={styles.child} />
        <StartScreen style={styles.child} navigation={navigation} />
      </SwiperFlatList>
    </View>
  );
};

export default Guide;

const { width } = Dimensions.get('window');

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  child: {
    width: width,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: Theme.colors.background,
  },
  text: {
    fontSize: 20,
    textAlign: 'center',
  },
});
