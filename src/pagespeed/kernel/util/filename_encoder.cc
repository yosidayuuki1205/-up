/*
 * Copyright 2010 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Author: sligocki@google.com (Shawn Ligocki)

#include "pagespeed/kernel/util/filename_encoder.h"
#include "pagespeed/kernel/base/string.h"
#include "pagespeed/kernel/base/string_util.h"

namespace net_instaweb {

FilenameEncoder::~FilenameEncoder() {
}

void FilenameEncoder::Encode(const StringPiece& filename_prefix,
                             const StringPiece& filename_ending,
                             GoogleString* encoded_filename) {
  UrlToFilenameEncoder::EncodeSegment(filename_prefix,
                                      filename_ending,
                                      '/', encoded_filename);
}

bool FilenameEncoder::Decode(const StringPiece& encoded_filename,
                             GoogleString* decoded_url) {
  return UrlToFilenameEncoder::Decode(encoded_filename, '/',
                                      decoded_url);
}

}  // namespace net_instaweb