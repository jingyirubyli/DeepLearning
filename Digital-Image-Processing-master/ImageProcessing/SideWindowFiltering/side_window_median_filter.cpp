#include "side_window_median_filter.h"
#include <algorithm>

static void sortArr(float *arr, int len) {
  const int middle = len / 2;
  for (int i = 0; i <= middle; ++i) {
    float min = arr[i];
    int min_idx = i;
    for (int j = i + 1; j < len; ++j) {
      if (min > arr[j]) {
        min_idx = j;
        min = arr[j];
      }
    }
    // swap idx i and min_idx
    float tmp = arr[min_idx];
    arr[min_idx] = arr[i];
    arr[i] = tmp;
  }
}

void SideWindowMedianFilter::fastSideWindowMedianFilter(const float  *input,
                                                        const int     radius,
                                                        const int     height,
                                                        const int     width,
                                                        float        *output) {
  int panel_size = height * width;       

  for (int i = 0; i < side_median_directions_count; ++i) {
    _sideWindowMedianFilterImpl(input, radius, height, width, static_cast<SIDE_MEDIAN_DIRECTIONS>(i), m_side_window_median_filter_results[i].data());
  }

  for (int i = 0; i < panel_size; ++i) {
    float tmp     = m_side_window_median_filter_results[0][i] - input[i];
    float min     = tmp * tmp;
    int   min_idx = 0;
    for (int j = 1; j < side_median_directions_count; ++j) {
      tmp = m_side_window_median_filter_results[j][i] - input[i];
      tmp = tmp * tmp;
      if (min > tmp) {
        min_idx = j;
        min = tmp;
      }
    }

    output[i] = m_side_window_median_filter_results[min_idx][i];
  }                                             
}

void SideWindowMedianFilter::_sideWindowMedianFilterImpl(const float                   *input,
                                                         const int                      radius,
                                                         const int                      height, 
                                                         const int                      width,
                                                         const SIDE_MEDIAN_DIRECTIONS   direction,
                                                         float                         *output) {
                              
  const int w_start = m_side_window_params[static_cast<int>(direction)][static_cast<int>(XY_START_END::WIDTH_START)];
  const int w_end   = m_side_window_params[static_cast<int>(direction)][static_cast<int>(XY_START_END::WIDTH_END)];
  const int h_start = m_side_window_params[static_cast<int>(direction)][static_cast<int>(XY_START_END::HEIGHT_START)];
  const int h_end   = m_side_window_params[static_cast<int>(direction)][static_cast<int>(XY_START_END::HEIGHT_END)];

  const int w_first_loop_end    = std::max(0, -w_start);
  const int w_second_loop_start = w_first_loop_end;
  const int w_second_loop_end   = width - 1 - w_end;
  const int w_third_loop_start  = width - w_end;

  int neon_width = w_second_loop_end - w_second_loop_start + 1;
  int nn = 0;
  int remain_start = (nn << 2) + w_second_loop_start;

  int out_idx = 0;
  for (int h = 0; h < height; ++h) {
    const int h_lower_bound = std::max(0, h + h_start);
    const int h_upper_bound = std::min(height - 1, h + h_end);
    const int h_interval = h_upper_bound - h_lower_bound + 1;

    for (int w = 0; w < w_first_loop_end; ++w) {
      const int w_left_bound = std::max(0, w + w_start);
      const int w_right_bound = std::min(width - 1, w + w_end);
      const int arr_len = h_interval * (w_right_bound - w_left_bound + 1);

      int idx = 0;
      for (int i = h_lower_bound; i <= h_upper_bound; ++i) {
        const int h_idx = i * width;
        for (int j = w_left_bound; j <= w_right_bound; ++j) {
          m_cache[idx ++] = input[h_idx + j];
        }
      }

      sortArr(m_cache.data(), arr_len);
      output[out_idx ++] = m_cache[arr_len / 2];
    }

    int remain_arr_len = h_interval * (w_end - w_start + 1);
    for (int w = remain_start; w <= w_second_loop_end; ++w) {
      const int w_left_bound = std::max(0, w + w_start);
      const int w_right_bound = std::min(width - 1, w + w_end);

      int idx = 0;
      for (int i = h_lower_bound; i <= h_upper_bound; ++i) {
        const int h_idx = i * width;
        for (int j = w_left_bound; j <= w_right_bound; ++j) {
          m_cache[idx ++] = input[h_idx + j];
        }
      }

      sortArr(m_cache.data(), remain_arr_len);
      output[out_idx ++] = m_cache[remain_arr_len / 2];
    }

    for (int w = w_third_loop_start; w < width; ++w) {
      const int w_left_bound = std::max(0, w + w_start);
      const int w_right_bound = std::min(width - 1, w + w_end);
      const int arr_len = h_interval * (w_right_bound - w_left_bound + 1);

      int idx = 0;
      for (int i = h_lower_bound; i <= h_upper_bound; ++i) {
        const int h_idx = i * width;
        for (int j = w_left_bound; j <= w_right_bound; ++j) {
          m_cache[idx ++] = input[h_idx + j];
        }
      }

      sortArr(m_cache.data(), arr_len);
      output[out_idx ++] = m_cache[arr_len / 2];
    }
  }                                 
}
